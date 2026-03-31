# GDS AI Skills

Expert GOV.UK Design System knowledge for AI coding assistants. Gives your AI tool accurate, up-to-date knowledge of [GDS Frontend v6.1.0](https://design-system.service.gov.uk/) — including the June 2025 Tudor Crown brand refresh — so it generates correct, accessible HTML for UK government service prototypes.

Supports **Claude Code**, **Cursor**, **GitHub Copilot**, **Windsurf**, and any tool that accepts a custom system prompt.

---

## What's included

### `gds-website-builder`
The main skill. Provides:
- All v6.1.0 breaking change rules (Tudor Crown SVG, `<div>` header/footer, Service navigation)
- Correct HTML for every component and page pattern
- WCAG 2.1 AA accessibility enforcement
- 111 pages of crawled GOV.UK Design System docs in `gds-docs/`

### `gds-docs-update`
Keeps the bundled docs fresh by re-crawling `design-system.service.gov.uk`. Run this whenever a new GDS version is released.

---

## Quick install

### Claude Code

**macOS / Linux:**
```bash
git clone https://github.com/Alearian/gds-ai-skills.git
cd gds-ai-skills
bash install.sh
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/Alearian/gds-ai-skills.git
cd gds-ai-skills
.\install.ps1
```

Restart Claude Code. That's it — the skills load automatically.

---

### Cursor

Install into your project directory:

**macOS / Linux:**
```bash
git clone https://github.com/Alearian/gds-ai-skills.git
cd gds-ai-skills
bash install.sh --tool cursor
```

**Windows:**
```powershell
git clone https://github.com/Alearian/gds-ai-skills.git
cd gds-ai-skills
.\install.ps1 -Tool cursor
```

This copies `gds-website-builder.mdc` into `.cursor/rules/` in the current directory. Cursor picks it up automatically — no restart needed.

**Optional:** Copy `gds-docs/` into your project for the AI to read full component HTML on demand:
```bash
cp -r gds-ai-skills/gds-website-builder/gds-docs ./gds-docs   # macOS/Linux
# or
Copy-Item -Recurse gds-ai-skills\gds-website-builder\gds-docs .\   # Windows
```

---

### GitHub Copilot

Install into your project directory:

**macOS / Linux:**
```bash
bash install.sh --tool copilot
```

**Windows:**
```powershell
.\install.ps1 -Tool copilot
```

This creates `.github/copilot-instructions.md` in the current directory. Copilot loads it automatically for every chat in that repo.

---

### Windsurf

Install into your project directory:

**macOS / Linux:**
```bash
bash install.sh --tool windsurf
```

**Windows:**
```powershell
.\install.ps1 -Tool windsurf
```

This creates `.windsurfrules` in the current directory. Windsurf loads it automatically.

---

### Any other tool (Zed, Aider, Continue, custom system prompt)

Copy the contents of `gds-website-builder/adapters/generic.md` into your tool's system prompt or custom instructions field.

---

## Using the skills

Once installed, just ask naturally:

> *"Build a question page asking for the user's date of birth"*
> *"Create a check-your-answers page"*
> *"Add a task list with three sections"*
> *"Fix the accessibility issues on this form"*
> *"Build a start page for a waste carrier registration service"*

**Claude Code only:** The AI will also read individual files from `gds-docs/` for full component HTML when needed (e.g. the complete Tudor Crown SVG, footer markup, date input).

**Other tools:** Point the AI at `gds-docs/components/<name>.md` or `gds-docs/patterns/<name>.md` for detailed HTML examples.

---

## Keeping docs up to date

When GOV.UK Frontend releases a new version:

**Claude Code:**
> *"Update the GDS docs"*

The `gds-docs-update` skill will start the crawl4ai Docker container and re-crawl all 111 pages. Requires Docker Desktop and Python 3.

**Other tools / manual:**
```bash
cd gds-ai-skills/gds-docs-update/scripts
pip install requests
docker run -d --name crawl4ai -p 11235:11235 unclecode/crawl4ai:latest
python crawl_site.py --output-dir ../gds-website-builder/gds-docs
```

After updating, check `gds-docs/community/whats-new.md` for breaking changes.

---

## Repo structure

```
README.md
install.sh                          macOS/Linux installer
install.ps1                         Windows installer

gds-website-builder/
  SKILL.md                          Claude Code skill definition
  README.md                         Skill-level readme
  gds-docs/                         111 crawled GOV.UK Design System pages
    components/  (34 files)
    patterns/    (29 files)
    styles/      (13 files)
    get-started/ (6 files)
    community/   (15 files)
    accessibility/
  adapters/
    cursor.mdc                      Cursor rules file (.cursor/rules/)
    copilot-instructions.md         GitHub Copilot (.github/copilot-instructions.md)
    windsurf.rules                  Windsurf (.windsurfrules)
    generic.md                      Any tool — paste as system prompt

gds-docs-update/
  SKILL.md                          Claude Code skill definition
  scripts/
    crawl_site.py                   Main crawl script
    site_pages.py                   Master list of 111 URLs
    process_md.py                   Markdown cleaner
    save_toplevel.py                Legacy script
```

---

## Notes

- The `gds-docs/` folder is committed to the repo so `gds-website-builder` works immediately after install, without needing to run a crawl.
- All content in `gds-docs/` is sourced from `https://design-system.service.gov.uk/` — Crown Copyright, used under the [Open Government Licence v3.0](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).
- This is an unofficial community tool and is not affiliated with CDDO or the GOV.UK Design System team.
