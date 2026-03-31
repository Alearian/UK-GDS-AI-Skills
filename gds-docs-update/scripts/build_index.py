"""
Generate DOCS_INDEX.md — a compact index of all locally-available GDS reference docs.

This lets the gds-website-builder skill discover what documentation is available
and load ONLY the specific file(s) it needs, rather than loading everything at once.

Paths resolved (in order of precedence):
  --gds-docs      <path>   Design System docs dir   (default: ../../gds-website-builder/gds-docs)
  --frontend-docs <path>   Frontend how-to docs dir (default: ../../gds-website-builder/gds-frontend-docs)
  --git-dir       <path>   Cloned git repo dir       (default: ../../gds-website-builder/gds_git/govuk-design-system)
  --output        <path>   Output file               (default: ../../gds-website-builder/DOCS_INDEX.md)

Usage:
    python build_index.py
    python build_index.py --output /path/to/DOCS_INDEX.md
"""

import os
import re
import sys

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_WB_DIR     = os.path.join(_SCRIPT_DIR, "..", "..", "gds-website-builder")

_DEFAULT_GDS_DOCS      = os.path.join(_WB_DIR, "gds-docs")
_DEFAULT_FRONTEND_DOCS = os.path.join(_WB_DIR, "gds-frontend-docs")
_DEFAULT_GIT_DIR       = os.path.join(_WB_DIR, "gds_git", "govuk-design-system")
_DEFAULT_OUTPUT        = os.path.join(_WB_DIR, "DOCS_INDEX.md")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_first_heading(filepath: str) -> str:
    """Return the first H1 or H2 heading from a markdown file, or a title-cased filename."""
    try:
        with open(filepath, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("# ") or line.startswith("## "):
                    heading = re.sub(r"^#{1,2}\s+", "", line)
                    # Truncate very long headings
                    return heading[:80] + ("…" if len(heading) > 80 else "")
    except Exception:
        pass
    return os.path.splitext(os.path.basename(filepath))[0].replace("-", " ").title()


def list_md_files(base_dir: str) -> list:
    """Return sorted list of (relative_path, heading) for all .md files under base_dir."""
    result = []
    if not os.path.isdir(base_dir):
        return result
    for root, dirs, files in os.walk(base_dir):
        dirs.sort()
        for fname in sorted(files):
            if fname.endswith(".md"):
                full = os.path.join(root, fname)
                rel  = os.path.relpath(full, base_dir).replace("\\", "/")
                result.append((rel, get_first_heading(full)))
    return result


def section_of(rel_path: str) -> str:
    """Return the top-level section name for a relative path."""
    parts = rel_path.split("/")
    if len(parts) == 1:
        return "root"
    top = parts[0]
    return top if not top.endswith(".md") else "root"


def list_git_highlights(git_dir: str) -> list:
    """Return brief notes about key directories in the cloned repo."""
    highlights = []
    if not os.path.isdir(git_dir):
        return highlights

    interesting = {
        "src":                  "SASS source files and compiled assets",
        "packages":             "Individual npm packages (govuk-frontend, etc.)",
        "app":                  "Local dev application and Nunjucks templates",
        "app/src/views":        "Nunjucks macro views for every component",
        "app/src/views/components": "Per-component Nunjucks macro files",
        "lib":                  "Build utilities and helpers",
        "docs":                 "Developer documentation",
    }

    for rel, description in interesting.items():
        full = os.path.join(git_dir, rel.replace("/", os.sep))
        if os.path.isdir(full):
            try:
                count = len(os.listdir(full))
                highlights.append((f"gds_git/govuk-design-system/{rel}/", description, count))
            except Exception:
                highlights.append((f"gds_git/govuk-design-system/{rel}/", description, "?"))

    return highlights


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = sys.argv[1:]

    def get_arg(flag, default):
        if flag in args:
            idx = args.index(flag)
            return os.path.abspath(args[idx + 1])
        return os.path.abspath(default)

    gds_docs      = get_arg("--gds-docs",      _DEFAULT_GDS_DOCS)
    frontend_docs = get_arg("--frontend-docs", _DEFAULT_FRONTEND_DOCS)
    git_dir       = get_arg("--git-dir",       _DEFAULT_GIT_DIR)
    output        = get_arg("--output",        _DEFAULT_OUTPUT)

    lines = []

    lines += [
        "# GDS Docs Index",
        "",
        "Auto-generated index of all locally-available GDS reference documentation.",
        "**Read this file first** to decide which specific docs file to load — then read only that file.",
        "",
        "---",
        "",
    ]

    # ── 1. Design System docs ─────────────────────────────────────────────
    lines += [
        "## 1. Design System docs (`gds-docs/`)",
        "",
        "Source: `https://design-system.service.gov.uk/`",
        "Components, patterns, styles, accessibility rules, and community pages.",
        "",
        "**Quick lookup rule:** to build a specific component, read `gds-docs/components/{name}.md`.",
        "To implement a pattern, read `gds-docs/patterns/{name}.md`.",
        "",
    ]

    gds_files = list_md_files(gds_docs)

    if gds_files:
        SECTION_ORDER = ["root", "get-started", "styles", "components", "patterns", "community", "accessibility"]
        grouped = {}
        for rel, heading in gds_files:
            s = section_of(rel)
            grouped.setdefault(s, []).append((rel, heading))

        for section in SECTION_ORDER:
            if section not in grouped:
                continue
            label = "Root / standalone pages" if section == "root" else section.replace("-", " ").title()
            lines.append(f"### {label}")
            lines.append("")
            for rel, heading in grouped[section]:
                lines.append(f"- `gds-docs/{rel}` — {heading}")
            lines.append("")

        # Any sections not in the standard order
        for section, items in grouped.items():
            if section not in SECTION_ORDER:
                lines.append(f"### {section}")
                lines.append("")
                for rel, heading in items:
                    lines.append(f"- `gds-docs/{rel}` — {heading}")
                lines.append("")
    else:
        lines += [
            "_Not yet crawled. Run `crawl_site.py` first:_",
            "```bash",
            "python crawl_site.py --output-dir %USERPROFILE%\\.claude\\skills\\gds-website-builder\\gds-docs",
            "```",
            "",
        ]

    # ── 2. Frontend how-to docs ────────────────────────────────────────────
    lines += [
        "---",
        "",
        "## 2. Frontend how-to docs (`gds-frontend-docs/`)",
        "",
        "Source: `https://frontend.design-system.service.gov.uk/`",
        "Installation, NPM setup, CSS/JS importing, JavaScript initialisation, configuration, and accessibility.",
        "",
        "**Quick lookup rule:** for any CSS/JS setup or configuration question, read from `gds-frontend-docs/`.",
        "",
    ]

    fe_files = list_md_files(frontend_docs)

    if fe_files:
        for rel, heading in fe_files:
            lines.append(f"- `gds-frontend-docs/{rel}` — {heading}")
        lines.append("")
    else:
        lines += [
            "_Not yet crawled. Run `crawl_frontend.py` first:_",
            "```bash",
            "python crawl_frontend.py --output-dir %USERPROFILE%\\.claude\\skills\\gds-website-builder\\gds-frontend-docs",
            "```",
            "",
        ]

    # ── 3. Git repo ────────────────────────────────────────────────────────
    lines += [
        "---",
        "",
        "## 3. Design System source repo (`gds_git/govuk-design-system/`)",
        "",
        "Source: `https://github.com/alphagov/govuk-design-system`",
        "Nunjucks macros, SASS, component fixtures, and full release history.",
        "",
        "**Quick lookup rule:** use Grep/Glob on `gds_git/govuk-design-system/` to find",
        "specific Nunjucks macros or SASS variables. Do NOT read whole directories.",
        "",
    ]

    git_highlights = list_git_highlights(git_dir)

    if git_highlights:
        lines.append("Key directories:")
        lines.append("")
        for path, description, count in git_highlights:
            lines.append(f"- `{path}` ({count} items) — {description}")
        lines.append("")
    else:
        lines += [
            "_Not yet cloned. Run `sync_git.py` first:_",
            "```bash",
            "python sync_git.py --target-dir %USERPROFILE%\\.claude\\skills\\gds-website-builder\\gds_git\\govuk-design-system",
            "```",
            "",
        ]

    # ── Usage summary ────────────────────────────────────────────────────
    lines += [
        "---",
        "",
        "## How to use this index",
        "",
        "1. Read `DOCS_INDEX.md` (this file) to see what is available.",
        "2. Identify the component, pattern, or topic needed.",
        "3. Read **only the specific file** — e.g. `gds-docs/components/button.md`.",
        "4. For NPM/CSS/JS setup, read from `gds-frontend-docs/`.",
        "5. For Nunjucks macros or SASS source, Grep `gds_git/govuk-design-system/`.",
        "",
        "Never load all docs at once. One file at a time keeps context lean.",
        "",
    ]

    # Write output
    content = "\n".join(lines)
    os.makedirs(os.path.dirname(output), exist_ok=True)
    with open(output, "w", encoding="utf-8") as f:
        f.write(content)

    total = len(gds_files) + len(fe_files)
    print(f"Index written to: {output}")
    print(f"  Design System docs : {len(gds_files)} files")
    print(f"  Frontend how-to    : {len(fe_files)} files")
    print(f"  Git repo           : {'present' if git_highlights else 'not cloned'}")
    print(f"  Total indexed      : {total} docs")


if __name__ == "__main__":
    main()
