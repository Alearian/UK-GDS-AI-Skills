"""
Crawl https://frontend.design-system.service.gov.uk/ via the local crawl4ai
Docker container (port 11235) and save cleaned markdown files to the output dir.

Auto-discovers pages by following internal links from the home page, then does
a second-pass to catch pages linked only from inner pages (e.g. accessibility/).

Output directory (in order of precedence):
  1. --output-dir <path>  (explicit override)
  2. Default: ../../gds-website-builder/gds-frontend-docs  relative to this script

Usage:
    python crawl_frontend.py                                    # crawl all pages
    python crawl_frontend.py --dry-run                          # print what would be fetched
    python crawl_frontend.py --output-dir C:/path/to/output    # write to specific dir
"""

import json
import os
import re
import sys
import time
import urllib.request
import urllib.error

CRAWL4AI_URL = "http://localhost:11235/md"
BASE = "https://frontend.design-system.service.gov.uk"
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_DEFAULT_OUTPUT = os.path.join(_SCRIPT_DIR, "..", "..", "gds-website-builder", "gds-frontend-docs")
DELAY = 0.5  # seconds between requests


# ---------------------------------------------------------------------------
# Fetch a page via crawl4ai — returns raw markdown, never passes through Claude
# ---------------------------------------------------------------------------

def fetch_markdown(url: str) -> str:
    """POST to crawl4ai /md endpoint; returns raw markdown string."""
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
# Page discovery — extract internal links from a crawled page
# ---------------------------------------------------------------------------

def extract_internal_links(raw_md: str) -> set:
    """Return all internal URLs (normalised, no anchors) found in markdown."""
    urls = set()
    for match in re.finditer(r"\[([^\]]*)\]\((https?://[^)]+)\)", raw_md):
        url = match.group(2).split("#")[0].rstrip("/") + "/"
        if url.startswith(BASE + "/") and url != BASE + "//":
            urls.add(url)
    return urls


def discover_pages() -> list:
    """
    Crawl the home page, extract links, then do one more pass over the found
    pages to catch any deeper pages not linked from the home page.
    Returns a sorted list of unique page URLs.
    """
    home = BASE + "/"
    print(f"Discovering pages from {home} ...")

    raw_home = fetch_markdown(home)
    urls = {home} | extract_internal_links(raw_home)
    print(f"  Home page yielded {len(urls)} URLs")

    # Second pass — crawl each non-home page once more to find deeper links
    second_pass_candidates = sorted(urls - {home})
    extra = set()
    for url in second_pass_candidates:
        try:
            time.sleep(DELAY)
            raw = fetch_markdown(url)
            new_links = extract_internal_links(raw) - urls
            extra.update(new_links)
        except Exception:
            pass  # discovery failures are non-fatal

    if extra:
        print(f"  Second pass found {len(extra)} additional URLs")
    urls.update(extra)

    result = sorted(urls)
    print(f"  Total pages discovered: {len(result)}")
    return result


# ---------------------------------------------------------------------------
# URL → local filepath
# ---------------------------------------------------------------------------

def url_to_filepath(url: str, output_dir: str) -> str:
    path = url[len(BASE):].strip("/")
    if not path:
        return os.path.join(output_dir, "index.md")
    # Nested paths like /accessibility/wcag-2.2/ → accessibility/wcag-2.2.md
    return os.path.join(output_dir, *path.split("/")[:-1], path.split("/")[-1] + ".md")


# ---------------------------------------------------------------------------
# Markdown cleaning
# ---------------------------------------------------------------------------

def clean_markdown(raw_md: str) -> str:
    """Strip navigation chrome and footer; rewrite internal links to relative .md paths."""
    lines = raw_md.split("\n")

    # Find start: after the last breadcrumb "1. [Home]", or first real heading
    start_idx = 0
    last_breadcrumb = 0
    for i, line in enumerate(lines):
        if line.strip().startswith("1. [Home]"):
            last_breadcrumb = i

    if last_breadcrumb > 0:
        start_idx = last_breadcrumb + 1
        while start_idx < len(lines) and (
            re.match(r"^\s*\d+\.\s", lines[start_idx]) or lines[start_idx].strip() == ""
        ):
            start_idx += 1
    else:
        # No breadcrumb — find first H1 after the initial nav block
        for i, line in enumerate(lines):
            if line.startswith("# ") and i > 5:
                start_idx = i
                break

    # Find end: before footer / support links
    end_idx = len(lines)
    for i, line in enumerate(lines):
        if line.strip() in ("## Support links", "## Footer"):
            end_idx = i
            break

    content = "\n".join(lines[start_idx:end_idx]).strip()

    # Rewrite absolute internal links to relative .md paths
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
        r"\[([^\]]*)\]\((https://frontend\.design-system\.service\.gov\.uk[^)]*)\)",
        convert_link,
        content,
    )

    # Remove back-to-top links
    content = re.sub(r"\[ \]\([^)]*#top\)", "", content)

    # Collapse excessive blank lines
    content = re.sub(r"\n{3,}", "\n\n", content)

    return content.strip() + "\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    dry_run = "--dry-run" in sys.argv

    output_dir = _DEFAULT_OUTPUT
    if "--output-dir" in sys.argv:
        idx = sys.argv.index("--output-dir")
        output_dir = os.path.abspath(sys.argv[idx + 1])
    else:
        output_dir = os.path.abspath(output_dir)

    print(f"Output directory: {output_dir}")

    urls = discover_pages()

    print(f"\nPages to crawl: {len(urls)}")

    if dry_run:
        for u in urls:
            print(f"  {url_to_filepath(u, output_dir)}")
        return

    os.makedirs(output_dir, exist_ok=True)

    ok = 0
    failed = []

    for i, url in enumerate(urls, 1):
        filepath = url_to_filepath(url, output_dir)
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
