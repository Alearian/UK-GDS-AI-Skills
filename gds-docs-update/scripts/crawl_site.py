"""
Crawl the entire GOV.UK Design System website via the local crawl4ai
Docker container (port 11235) and save cleaned markdown files to the output dir.

Output directory (in order of precedence):
  1. --output-dir <path>  (explicit override)
  2. Default: ../gds-docs  relative to this script
     i.e. C:\\Users\\Develepor\\.claude\\skills\\gds-docs

Usage:
    python crawl_site.py                                          # crawl all pages
    python crawl_site.py --section components                     # crawl one section only
    python crawl_site.py --dry-run                                # just print what would be fetched
    python crawl_site.py --sync                                   # fetch live sitemap, detect new/deleted pages, then crawl
    python crawl_site.py --output-dir C:/path/to/gds-docs         # write to a specific directory
"""

import json
import os
import re
import sys
import time
import urllib.request
import urllib.error

from site_pages import PAGES, BASE, all_pages

CRAWL4AI_URL = "http://localhost:11235/md"
_DEFAULT_DOCS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "gds-docs")
DELAY = 0.5  # seconds between requests (be polite)


# ---------------------------------------------------------------------------
# Markdown cleaning  (inlined from process_md.py to keep this self-contained)
# ---------------------------------------------------------------------------

def clean_markdown(raw_md: str) -> str:
    """Strip nav chrome, cookie banners, footer; fix links to relative .md."""
    lines = raw_md.split("\n")

    # ---- find start of main content ----
    start_idx = 0

    # First pass: skip duplicate nav blocks that appear before content.
    # The raw markdown repeats the full nav twice (mobile + desktop).
    # Content starts after the *last* breadcrumb "1. [Home]".
    last_breadcrumb = 0
    for i, line in enumerate(lines):
        if line.strip().startswith("1. [Home]"):
            last_breadcrumb = i

    if last_breadcrumb > 0:
        start_idx = last_breadcrumb + 1
        # Skip remaining breadcrumb numbered lines and blanks
        while start_idx < len(lines) and (
            re.match(r"^\s*\d+\.\s", lines[start_idx]) or lines[start_idx].strip() == ""
        ):
            start_idx += 1
    else:
        # Home page or pages without breadcrumbs
        for i, line in enumerate(lines):
            if "# Design your service" in line or (line.startswith("#  ") and i > 50):
                start_idx = i
                break

    # ---- find end of main content (before footer) ----
    end_idx = len(lines)
    for i, line in enumerate(lines):
        if line.strip() == "## Support links":
            end_idx = i
            break

    content = "\n".join(lines[start_idx:end_idx]).strip()

    # ---- convert absolute links to relative .md paths ----
    def convert_link(match):
        text = match.group(1)
        url = match.group(2)
        if url.startswith(BASE):
            path = url[len(BASE):]
            if not path or path == "/":
                return f"[{text}](./index.md)"
            path = path.strip("/")
            return f"[{text}](./{path}.md)"
        return match.group(0)

    content = re.sub(
        r"\[([^\]]*)\]\((https://design-system\.service\.gov\.uk[^)]*)\)",
        convert_link,
        content,
    )

    # Remove back-to-top links
    content = re.sub(r"\[ \]\([^)]*#top\)", "", content)

    # Collapse excessive blank lines
    content = re.sub(r"\n{3,}", "\n\n", content)

    return content.strip() + "\n"


# ---------------------------------------------------------------------------
# URL -> local filepath
# ---------------------------------------------------------------------------

def url_to_filepath(url: str) -> str:
    path = url[len(BASE):].strip("/")
    if not path:
        return os.path.join(DOCS_DIR, "index.md")
    return os.path.join(DOCS_DIR, f"{path}.md")


# ---------------------------------------------------------------------------
# Fetch a single page from crawl4ai
# ---------------------------------------------------------------------------

def fetch_markdown(url: str) -> str:
    """Call crawl4ai /md endpoint and return the raw markdown string."""
    payload = json.dumps({"url": url, "f": "raw"}).encode("utf-8")
    req = urllib.request.Request(
        CRAWL4AI_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    resp = urllib.request.urlopen(req, timeout=60)
    data = json.loads(resp.read().decode("utf-8"))
    if not data.get("success"):
        raise RuntimeError(f"crawl4ai failed for {url}: {data}")
    return data["markdown"]


# ---------------------------------------------------------------------------
# Live sitemap extraction  (--sync mode)
# ---------------------------------------------------------------------------

def extract_live_sitemap() -> set:
    """Fetch the /sitemap/ page via crawl4ai and extract all internal URLs."""
    sitemap_url = f"{BASE}/sitemap/"
    print(f"Fetching live sitemap from {sitemap_url} ...")
    raw_md = fetch_markdown(sitemap_url)

    urls = set()
    # Match all markdown links pointing to the GDS site
    for match in re.finditer(r"\[([^\]]*)\]\((https://design-system\.service\.gov\.uk[^)]*)\)", raw_md):
        url = match.group(2)
        # Normalise: strip anchors, ensure trailing slash
        url = url.split("#")[0].rstrip("/") + "/"
        urls.add(url)

    # Also add the well-known pages that appear in the footer but not the
    # main sitemap listing (they're in the "Support links" section)
    for suffix in ["sitemap/", "cookies/", "accessibility-statement/",
                    "privacy-policy/", "contact/", "design-system-team/"]:
        urls.add(f"{BASE}/{suffix}")

    # Always include the homepage
    urls.add(f"{BASE}/")

    return urls


def classify_url(url: str) -> str:
    """Return the site_pages section name for a URL."""
    path = url[len(BASE):].strip("/")
    if not path:
        return "root"
    top = path.split("/")[0]
    section_map = {
        "get-started": "get-started",
        "styles": "styles",
        "components": "components",
        "patterns": "patterns",
        "community": "community",
        "accessibility": "accessibility",
    }
    return section_map.get(top, "root")


def sync_sitemap():
    """Compare live sitemap with site_pages.py and report differences."""
    live_urls = extract_live_sitemap()

    known_set = set()
    for url in all_pages():
        known_set.add(url.rstrip("/") + "/")

    new_urls = sorted(live_urls - known_set)
    deleted_urls = sorted(known_set - live_urls)

    print(f"\nLive sitemap: {len(live_urls)} pages")
    print(f"site_pages.py: {len(known_set)} pages")

    if new_urls:
        print(f"\n  NEW pages found ({len(new_urls)}):")
        for u in new_urls:
            section = classify_url(u)
            print(f"    + {u}  (section: {section})")
        print("\n  --> Add these to site_pages.py in the appropriate section,")
        print("      then re-run to crawl them.")
    else:
        print("\n  No new pages found.")

    if deleted_urls:
        print(f"\n  REMOVED pages ({len(deleted_urls)}):")
        for u in deleted_urls:
            filepath = url_to_filepath(u)
            exists = " (local file exists)" if os.path.exists(filepath) else ""
            print(f"    - {u}{exists}")
        print("\n  --> Consider removing these from site_pages.py and deleting")
        print("      the corresponding .md files from docs/.")
    else:
        print("\n  No removed pages detected.")

    if not new_urls and not deleted_urls:
        print("\n  site_pages.py is up to date with the live site.")

    return new_urls, deleted_urls


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    dry_run = "--dry-run" in sys.argv
    do_sync = "--sync" in sys.argv
    section_filter = None
    if "--section" in sys.argv:
        idx = sys.argv.index("--section")
        section_filter = sys.argv[idx + 1]

    # Allow caller to override output directory
    global DOCS_DIR
    if "--output-dir" in sys.argv:
        idx = sys.argv.index("--output-dir")
        DOCS_DIR = os.path.abspath(sys.argv[idx + 1])
    else:
        DOCS_DIR = os.path.abspath(_DEFAULT_DOCS_DIR)

    # If --sync, check the live sitemap first
    if do_sync:
        new_urls, deleted_urls = sync_sitemap()
        if new_urls:
            print("\nWARNING: New pages exist on the live site that are not in site_pages.py.")
            print("They will NOT be crawled until you add them. Continuing with known pages...\n")
        if not dry_run:
            print()  # blank line before crawl output

    # Build URL list
    if section_filter:
        if section_filter not in PAGES:
            print(f"Unknown section '{section_filter}'. Available: {list(PAGES.keys())}")
            sys.exit(1)
        urls = PAGES[section_filter]
    else:
        urls = all_pages()

    print(f"Pages to crawl: {len(urls)}")
    if dry_run:
        for u in urls:
            print(f"  {url_to_filepath(u)}")
        return

    # Ensure docs dir exists
    os.makedirs(DOCS_DIR, exist_ok=True)

    ok = 0
    failed = []

    for i, url in enumerate(urls, 1):
        filepath = url_to_filepath(url)
        label = url.replace(BASE, "") or "/"
        print(f"[{i:3d}/{len(urls)}] {label} ... ", end="", flush=True)

        try:
            raw_md = fetch_markdown(url)
            cleaned = clean_markdown(raw_md)

            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(cleaned)

            ok += 1
            print(f"OK  ({len(cleaned):,} chars)")
        except Exception as e:
            failed.append((url, str(e)))
            print(f"FAILED  ({e})")

        if i < len(urls):
            time.sleep(DELAY)

    print(f"\nDone. {ok} succeeded, {len(failed)} failed.")
    if failed:
        print("\nFailed pages:")
        for url, err in failed:
            print(f"  {url}  ->  {err}")


if __name__ == "__main__":
    main()
