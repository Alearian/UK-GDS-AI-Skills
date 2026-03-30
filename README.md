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
git clone https://github.com/YOUR_USERNAME/gds-ai-skills.git
cd gds-ai-skills
bash install.sh
```

**Windows (PowerShell):**
```powershell
git clone https://github.com/YOUR_USERNAME/gds-ai-skills.git
cd gds-ai-skills
.\install.ps1
```

Restart Claude Code. That's it — the skills load automatically.

---

### Cursor

Install into your project directory:

**macOS / Linux:**
```bash
git clone https://github.com/YOUR_USERNAME/gds-ai-skills.git
cd gds-ai-skills
bash install.sh --tool cursor
```

**Windows:**
```powershell
git clone https://github.com/YOUR_USERNAME/gds-ai-skills.git
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

When GOV.UK Frontend releases a new version, re-crawl the design system to update the bundled docs. This requires Docker Desktop and Python 3 — see [Setting up crawl4ai](#setting-up-crawl4ai) below.

**Claude Code (with Docker MCP):**
> *"Update the GDS docs"*

The `gds-docs-update` skill handles everything — starts the container if needed, crawls all 111 pages, and writes the results to `gds-website-builder/gds-docs/`.

**Claude Code (without Docker MCP) / manual:**
```bash
# Start crawl4ai if not already running
docker start crawl4ai || docker run -d --name crawl4ai --restart unless-stopped -p 11235:11235 unclecode/crawl4ai:latest

# Run the crawl
cd gds-docs-update/scripts
python crawl_site.py --output-dir ../gds-website-builder/gds-docs
```

**Windows (PowerShell):**
```powershell
docker start crawl4ai
cd gds-docs-update\scripts
python crawl_site.py --output-dir ..\gds-website-builder\gds-docs
```

After updating, check `gds-website-builder/gds-docs/community/whats-new.md` for breaking changes and update the version number in `gds-website-builder/SKILL.md` if needed.

---

## Setting up crawl4ai

[crawl4ai](https://github.com/unclecode/crawl4ai) is an open-source web crawler that runs in Docker. It is only needed for the `gds-docs-update` skill — the main `gds-website-builder` skill works out of the box without it.

**Prerequisite:** [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running.

---

### Option A — Claude Code with Docker MCP (easiest)

If you have the Docker MCP server configured in Claude Code, just say:

> *"Set up the crawl4ai Docker container"*

Claude will pull the image, create the container, and confirm it is healthy — no terminal needed.

**To add the Docker MCP to Claude Code:**
```bash
claude mcp add docker -- docker run -i --rm -v /var/run/docker.sock:/var/run/docker.sock mcp/docker
```
> **Windows:** replace `/var/run/docker.sock` with `//./pipe/docker_engine`

---

### Option B — Terminal / PowerShell

**macOS / Linux:**
```bash
# Create and start the container (only needed once)
docker run -d --name crawl4ai --restart unless-stopped -p 11235:11235 unclecode/crawl4ai:latest

# Wait ~20 seconds, then verify it is healthy
curl http://localhost:11235/health
# Expected: {"status":"ok",...}
```

**Windows (PowerShell):**
```powershell
# Create and start the container (only needed once)
docker run -d --name crawl4ai --restart unless-stopped -p 11235:11235 unclecode/crawl4ai:latest

# Wait ~20 seconds, then verify it is healthy
Invoke-RestMethod -Uri "http://localhost:11235/health"
# Expected: status : ok
```

The `--restart unless-stopped` flag means the container starts automatically with Docker Desktop on future boots.

---

### Starting an existing container

If you have set up crawl4ai before and it is currently stopped:

```bash
docker start crawl4ai
```

---

### Updating crawl4ai to the latest version

```bash
docker stop crawl4ai && docker rm crawl4ai
docker pull unclecode/crawl4ai:latest
docker run -d --name crawl4ai --restart unless-stopped -p 11235:11235 unclecode/crawl4ai:latest
```

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
