---
name: gds-docs-update
description: >
  Maintains a local markdown mirror of the GOV.UK Design System website by
  crawling design-system.service.gov.uk using the crawl4ai Docker container,
  crawling the GOV.UK Frontend how-to site (frontend.design-system.service.gov.uk),
  cloning the alphagov/govuk-design-system GitHub repository locally, and
  generating a DOCS_INDEX.md so the gds-website-builder skill can load docs selectively.

  Always use this skill when the user asks to:
  - Update or refresh the GDS docs
  - Re-crawl the GOV.UK Design System website
  - Sync the local GDS markdown docs
  - Check for changes on design-system.service.gov.uk or frontend.design-system.service.gov.uk
  - Add missing GDS pages to the local docs mirror
  - Run crawl_site.py, crawl_frontend.py, sync_git.py, or build_index.py
  - Set up, start, or install the crawl4ai Docker container
  - Install or configure crawl4ai
  - Clone or update the govuk-design-system git repository
  - Rebuild or refresh DOCS_INDEX.md

  Also trigger for: update gds docs, refresh gds, crawl gds, sync gds,
  gds docs update, re-crawl design system, update design system docs,
  gds mirror, local gds copy, set up crawl4ai, install crawl4ai, crawl4ai container,
  clone govuk design system, sync git repo, update frontend docs, frontend how-to
---

# GDS Docs Update Skill

This skill maintains three local reference sources for the gds-website-builder skill:

| Source | Script | Output |
|---|---|---|
| Design System website (111 pages) | `crawl_site.py` | `gds-website-builder/gds-docs/` |
| Frontend how-to website | `crawl_frontend.py` | `gds-website-builder/gds-frontend-docs/` |
| GitHub source repo | `sync_git.py` | `gds-website-builder/gds_git/govuk-design-system/` |
| Docs index (selective loading) | `build_index.py` | `gds-website-builder/DOCS_INDEX.md` |

> **All scripts run locally and pipe content directly to disk — nothing passes through Claude as tokens.**

## Key paths

| Item | Path |
|---|---|
| Scripts | `~/.claude/skills/gds-docs-update/scripts/` |
| Design System docs | `~/.claude/skills/gds-website-builder/gds-docs/` |
| Frontend how-to docs | `~/.claude/skills/gds-website-builder/gds-frontend-docs/` |
| Git repo | `~/.claude/skills/gds-website-builder/gds_git/govuk-design-system/` |
| Docs index | `~/.claude/skills/gds-website-builder/DOCS_INDEX.md` |
| crawl4ai port | `http://localhost:11235` |

> **Windows users:** replace `~` with `%USERPROFILE%` (e.g. `C:\Users\YourName`)

---

## Environment guidance

| Environment | Docker | Script execution |
|---|---|---|
| **Claude Code** | Use `mcp__MCP_DOCKER__docker` MCP tool | Use Bash tool directly |
| **Cowork / Claude.ai** | Provide PowerShell commands for user to run | Provide PowerShell commands for user to run |

---

## Step 1 — Ensure crawl4ai Docker container is running

*(Required for Steps 2 and 3 only. Steps 4 and 5 do not need Docker.)*

### Claude Code: use the Docker MCP tool

Check if the container is already running:

```
mcp__MCP_DOCKER__docker  {"cmd": ["ps", "--filter", "name=crawl4ai", "--format", "{{.Status}}"]}
```

- If output contains `Up` → container is running, skip to Step 2.
- If output is empty → container exists but is stopped, start it:

```
mcp__MCP_DOCKER__docker  {"cmd": ["start", "crawl4ai"]}
```

- If you get an error saying the container does not exist → create and start it:

```
mcp__MCP_DOCKER__docker  {"cmd": ["run", "-d", "--name", "crawl4ai", "-p", "11235:11235", "unclecode/crawl4ai:latest"]}
```

After starting, wait for the health endpoint:

```bash
for i in $(seq 1 15); do
  result=$(curl -s http://localhost:11235/health 2>/dev/null)
  if echo "$result" | grep -q '"status"'; then
    echo "Ready: $result"
    break
  fi
  sleep 2
done
```

### Cowork / Claude.ai: provide these PowerShell commands to the user

```powershell
docker ps --filter "name=crawl4ai" --format "{{.Status}}"
# If stopped: docker start crawl4ai
# If missing:  docker run -d --name crawl4ai -p 11235:11235 unclecode/crawl4ai:latest

$ready = $false
for ($i = 0; $i -lt 15 -and -not $ready; $i++) {
    try {
        $r = Invoke-RestMethod -Uri "http://localhost:11235/health" -ErrorAction Stop
        Write-Host ($r | ConvertTo-Json -Compress); $ready = $true
    } catch { Start-Sleep -Seconds 2 }
}
if (-not $ready) { Write-Warning "crawl4ai did not become healthy in time." }
```

---

## Step 2 — Crawl the Design System website

*(Requires crawl4ai — see Step 1)*

### Claude Code

```bash
cd %USERPROFILE%\.claude\skills\gds-docs-update\scripts

# Full re-crawl (all 111 pages, ~2 minutes)
python crawl_site.py --output-dir %USERPROFILE%\.claude\skills\gds-website-builder\gds-docs

# Single section only
python crawl_site.py --section components  --output-dir %USERPROFILE%\.claude\skills\gds-website-builder\gds-docs
python crawl_site.py --section patterns    --output-dir %USERPROFILE%\.claude\skills\gds-website-builder\gds-docs
python crawl_site.py --section styles      --output-dir %USERPROFILE%\.claude\skills\gds-website-builder\gds-docs
python crawl_site.py --section get-started --output-dir %USERPROFILE%\.claude\skills\gds-website-builder\gds-docs
python crawl_site.py --section community   --output-dir %USERPROFILE%\.claude\skills\gds-website-builder\gds-docs
python crawl_site.py --section accessibility --output-dir %USERPROFILE%\.claude\skills\gds-website-builder\gds-docs

# Check for new/removed pages without crawling
python crawl_site.py --sync --dry-run --output-dir %USERPROFILE%\.claude\skills\gds-website-builder\gds-docs
```

### Cowork / Claude.ai

```powershell
cd "$env:USERPROFILE\.claude\skills\gds-docs-update\scripts"
python crawl_site.py --output-dir "$env:USERPROFILE\.claude\skills\gds-website-builder\gds-docs"
```

---

## Step 3 — Crawl the Frontend how-to website

*(Requires crawl4ai — see Step 1)*

Crawls `https://frontend.design-system.service.gov.uk/` — auto-discovers all pages by
following internal links from the home page.

### Claude Code

```bash
cd %USERPROFILE%\.claude\skills\gds-docs-update\scripts

# Full crawl (auto-discovers all pages)
python crawl_frontend.py --output-dir %USERPROFILE%\.claude\skills\gds-website-builder\gds-frontend-docs

# Dry run — print what would be fetched without crawling
python crawl_frontend.py --dry-run --output-dir %USERPROFILE%\.claude\skills\gds-website-builder\gds-frontend-docs
```

### Cowork / Claude.ai

```powershell
cd "$env:USERPROFILE\.claude\skills\gds-docs-update\scripts"
python crawl_frontend.py --output-dir "$env:USERPROFILE\.claude\skills\gds-website-builder\gds-frontend-docs"
```

---

## Step 4 — Clone / update the GitHub source repo

*(Does NOT require crawl4ai — uses git directly)*

Clones `https://github.com/alphagov/govuk-design-system` locally.
Run once with `--shallow`; subsequent runs do `git pull` automatically.

### Claude Code

```bash
cd %USERPROFILE%\.claude\skills\gds-docs-update\scripts

# First time — use --shallow for a faster clone (~50 MB vs ~200 MB)
python sync_git.py --shallow --target-dir %USERPROFILE%\.claude\skills\gds-website-builder\gds_git\govuk-design-system

# Subsequent runs — just pull latest changes
python sync_git.py --target-dir %USERPROFILE%\.claude\skills\gds-website-builder\gds_git\govuk-design-system
```

### Cowork / Claude.ai

```powershell
cd "$env:USERPROFILE\.claude\skills\gds-docs-update\scripts"

# First time
python sync_git.py --shallow `
  --target-dir "$env:USERPROFILE\.claude\skills\gds-website-builder\gds_git\govuk-design-system"

# Subsequent updates
python sync_git.py `
  --target-dir "$env:USERPROFILE\.claude\skills\gds-website-builder\gds_git\govuk-design-system"
```

---

## Step 5 — Rebuild the docs index

*(Run after any of Steps 2–4 to keep DOCS_INDEX.md current)*

Generates `DOCS_INDEX.md` — a compact index of every available doc with its file path
and heading. The website-builder skill reads this first to find the right file without
loading all docs.

### Claude Code

```bash
cd %USERPROFILE%\.claude\skills\gds-docs-update\scripts

python build_index.py ^
  --gds-docs      %USERPROFILE%\.claude\skills\gds-website-builder\gds-docs ^
  --frontend-docs %USERPROFILE%\.claude\skills\gds-website-builder\gds-frontend-docs ^
  --git-dir       %USERPROFILE%\.claude\skills\gds-website-builder\gds_git\govuk-design-system ^
  --output        %USERPROFILE%\.claude\skills\gds-website-builder\DOCS_INDEX.md
```

### Cowork / Claude.ai

```powershell
cd "$env:USERPROFILE\.claude\skills\gds-docs-update\scripts"
python build_index.py `
  --gds-docs      "$env:USERPROFILE\.claude\skills\gds-website-builder\gds-docs" `
  --frontend-docs "$env:USERPROFILE\.claude\skills\gds-website-builder\gds-frontend-docs" `
  --git-dir       "$env:USERPROFILE\.claude\skills\gds-website-builder\gds_git\govuk-design-system" `
  --output        "$env:USERPROFILE\.claude\skills\gds-website-builder\DOCS_INDEX.md"
```

---

## Full update workflow (all sources)

Run all five steps in sequence to bring everything up to date:

### Claude Code (bash)

```bash
cd %USERPROFILE%\.claude\skills\gds-docs-update\scripts
set WB=%USERPROFILE%\.claude\skills\gds-website-builder

python crawl_site.py     --output-dir %WB%\gds-docs
python crawl_frontend.py --output-dir %WB%\gds-frontend-docs
python sync_git.py       --target-dir %WB%\gds_git\govuk-design-system
python build_index.py    --gds-docs %WB%\gds-docs --frontend-docs %WB%\gds-frontend-docs ^
                         --git-dir %WB%\gds_git\govuk-design-system --output %WB%\DOCS_INDEX.md
```

After running, check `gds-docs/community/whats-new.md` for breaking changes and update
`gds-website-builder/SKILL.md` if the version number or component rules have changed.

---

## Scripts reference

| Script | Purpose |
|---|---|
| `crawl_site.py` | Crawls all 111 pages of design-system.service.gov.uk. Accepts `--output-dir`, `--section`, `--dry-run`, `--sync`. |
| `site_pages.py` | Master list of all 111 Design System page URLs, organised by section. |
| `crawl_frontend.py` | Auto-discovers and crawls all pages on frontend.design-system.service.gov.uk. Accepts `--output-dir`, `--dry-run`. |
| `sync_git.py` | Clones or pulls the alphagov/govuk-design-system GitHub repo. Accepts `--target-dir`, `--shallow`. |
| `build_index.py` | Generates DOCS_INDEX.md listing every available doc. Accepts `--gds-docs`, `--frontend-docs`, `--git-dir`, `--output`. |
| `process_md.py` | Standalone markdown cleaner — reads JSON from stdin. One-off use. |
| `save_toplevel.py` | Legacy script. Superseded by `crawl_site.py`. |

---

## Adding a new Design System page

1. Edit `site_pages.py` — add the URL to the appropriate section in the `PAGES` dict.
2. Run `crawl_site.py --section <section>` to fetch it.
3. Run `build_index.py` to update the index.

---

## Markdown cleaning rules

The `clean_markdown()` functions (in `crawl_site.py` and `crawl_frontend.py`):

- Find the last `1. [Home]` breadcrumb and start content after it
- Fall back to the first H1 heading for pages without breadcrumbs
- Stop at `## Support links` (footer)
- Convert all internal absolute links to relative `./path.md` links
- Remove `[ ](#top)` back-to-top links
- Collapse 3+ consecutive blank lines to 2

---

## Output structure

```
~/.claude/skills/gds-website-builder/
  DOCS_INDEX.md                        ← read this first (selective loading map)
  gds-docs/                            ← Design System website (111 pages)
    index.md  sitemap.md  cookies.md ...
    get-started/   styles/   components/   patterns/   community/   accessibility/
  gds-frontend-docs/                   ← Frontend how-to website (auto-discovered)
    index.md
    get-started.md
    installing-with-npm.md
    importing-css.md
    importing-javascript.md
    configure-components.md
    ...
  gds_git/
    govuk-design-system/               ← GitHub source repo (git clone)
      app/src/views/components/        ← Nunjucks macros per component
      src/                             ← SASS source
      packages/                        ← npm packages
      ...
```
