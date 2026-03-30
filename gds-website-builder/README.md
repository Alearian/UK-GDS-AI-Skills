# GDS Website Builder — Claude Code Skill

A [Claude Code](https://claude.ai/claude-code) skill that gives Claude expert knowledge of the [GOV.UK Design System](https://design-system.service.gov.uk/) (GDS Frontend v6.1.0), enabling it to build fully compliant GOV.UK prototype websites using plain HTML and `govuk-*` CSS classes.

The `gds-docs-update` companion skill keeps the bundled docs fresh by re-crawling the live GOV.UK Design System website whenever a new version is released.

---

## What these skills do

### `gds-website-builder`
- Generates correct, accessible HTML for every GDS component and page pattern
- Knows all **v6.1.0 breaking changes** (Tudor Crown SVG, `<div>` header/footer, Service navigation component)
- Reads the bundled `gds-docs/` folder for authoritative, up-to-date HTML examples — no hallucination from training data
- Enforces WCAG 2.1 AA accessibility rules throughout
- Outputs TypeScript-compatible HTML — **no Nunjucks**

### `gds-docs-update`
- Crawls all 111 pages of `https://design-system.service.gov.uk/` using the [crawl4ai](https://github.com/unclecode/crawl4ai) Docker container
- Cleans and saves markdown to `gds-website-builder/gds-docs/` so the main skill always has the latest docs
- Supports full re-crawl or single-section updates

---

## Installation

### Prerequisites
- [Claude Code](https://claude.ai/claude-code) installed
- Python 3.8+ (for `gds-docs-update` only)
- Docker Desktop (for `gds-docs-update` only)

### Install the skills

**macOS / Linux:**
```bash
# Create skills directory if it doesn't exist
mkdir -p ~/.claude/skills

# Clone the repo directly into the skills directory
git clone https://github.com/YOUR_USERNAME/claude-gds-skills.git ~/.claude/skills/claude-gds-skills

# Symlink (or copy) the two skill folders into place
ln -s ~/.claude/skills/claude-gds-skills/gds-website-builder ~/.claude/skills/gds-website-builder
ln -s ~/.claude/skills/claude-gds-skills/gds-docs-update    ~/.claude/skills/gds-docs-update
```

Or simply copy the folders manually:
```bash
cp -r gds-website-builder ~/.claude/skills/
cp -r gds-docs-update     ~/.claude/skills/
```

**Windows (PowerShell):**
```powershell
# Copy the skill folders
Copy-Item -Recurse gds-website-builder "$env:USERPROFILE\.claude\skills\"
Copy-Item -Recurse gds-docs-update     "$env:USERPROFILE\.claude\skills\"
```

That's it. Restart Claude Code and the skills will be available immediately.

---

## Using `gds-website-builder`

Just ask Claude Code to build or review GDS pages naturally:

> "Build a question page asking for the user's date of birth"
> "Create a check-your-answers page for my registration service"
> "Add a task list to my service with three sections"
> "Fix the accessibility issues on this form"

Claude will automatically load the skill and read the relevant `gds-docs/` files before generating HTML.

---

## Using `gds-docs-update`

Run this whenever GOV.UK Frontend releases a new version to update the bundled docs:

> "Update the GDS docs"
> "Re-crawl the design system"

Requirements:
- Docker Desktop must be running
- Python packages: `pip install requests`

The skill will start the crawl4ai Docker container and re-crawl all 111 pages, writing the results to `gds-website-builder/gds-docs/`.

---

## Repo structure

```
gds-website-builder/
  SKILL.md              — Main skill definition loaded by Claude Code
  gds-docs/             — Bundled GOV.UK Design System docs (111 markdown files)
    components/         — 34 component pages
    patterns/           — 29 pattern pages
    styles/             — 13 style pages
    get-started/        — 6 get-started pages
    community/          — 15 community pages
    accessibility/      — 1 accessibility page

gds-docs-update/
  SKILL.md              — Docs-update skill definition
  scripts/
    crawl_site.py       — Main crawl script
    site_pages.py       — Master list of all 111 URLs
    process_md.py       — Markdown cleaner
    save_toplevel.py    — Legacy script
```

---

## Keeping docs up to date

When GOV.UK Frontend releases a new version:

1. Ask Claude: *"Update the GDS docs"*
2. Review `gds-docs/community/whats-new.md` for breaking changes
3. If the version number or breaking-change rules have changed, ask Claude: *"Update the gds-website-builder skill for the new version"*

---

## Notes

- The `gds-docs/` folder is intentionally committed to the repo so that `gds-website-builder` works immediately after install without needing to run a crawl
- The docs were crawled from `https://design-system.service.gov.uk/` — all content belongs to the GOV.UK Design System team (Crown Copyright)
- This repo is an unofficial community tool and is not affiliated with CDDO or the GOV.UK Design System team
