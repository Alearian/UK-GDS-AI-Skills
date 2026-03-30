---
name: gds-docs-update
description: >
  Maintains a local markdown mirror of the GOV.UK Design System website by
  crawling design-system.service.gov.uk using the crawl4ai Docker container
  and the Python scripts in the gds-docs-update/scripts/ skill folder.

  Always use this skill when the user asks to:
  - Update or refresh the GDS docs
  - Re-crawl the GOV.UK Design System website
  - Sync the local GDS markdown docs
  - Check for changes on design-system.service.gov.uk
  - Add missing GDS pages to the local docs mirror
  - Run crawl_site.py or site_pages.py

  Also trigger for: update gds docs, refresh gds, crawl gds, sync gds,
  gds docs update, re-crawl design system, update design system docs,
  gds mirror, local gds copy
---

# GDS Docs Update Skill

This skill maintains a local markdown mirror of every page on
`https://design-system.service.gov.uk/` (111 pages across 7 sections).

## Key paths

| Item | Path |
|---|---|
| Scripts | `~/.claude/skills/gds-docs-update/scripts/` |
| Output (docs) | `~/.claude/skills/gds-website-builder/gds-docs/` |
| crawl4ai port | `http://localhost:11235` |

> **Windows users:** replace `~` with `%USERPROFILE%` (e.g. `C:\Users\YourName`)

---

## Environment guidance

This skill works in all Claude environments. The approach differs by environment:

| Environment | Docker | Script execution |
|---|---|---|
| **Claude Code** | Use `mcp__MCP_DOCKER__docker` MCP tool | Use Bash tool directly |
| **Cowork** | Provide PowerShell commands for user to run | Provide PowerShell commands for user to run |
| **Claude.ai (web)** | Provide PowerShell commands for user to run | Provide PowerShell commands for user to run |

---

## Step 1 — Ensure crawl4ai Docker container is running

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

After starting, wait for the health endpoint. Poll with the Bash tool:

```bash
# Poll http://localhost:11235/health up to 30 seconds
for i in $(seq 1 15); do
  result=$(curl -s http://localhost:11235/health 2>/dev/null)
  if echo "$result" | grep -q '"status"'; then
    echo "Ready: $result"
    break
  fi
  sleep 2
done
```

Only proceed once you see `"status":"ok"` in the output.

### Cowork / Claude.ai: provide these PowerShell commands to the user

```powershell
# Check if running
docker ps --filter "name=crawl4ai" --format "{{.Status}}"

# If stopped (container exists):
docker start crawl4ai

# If container does not exist yet:
docker run -d --name crawl4ai -p 11235:11235 unclecode/crawl4ai:latest

# Wait for health (retry up to 30 seconds)
$ready = $false
for ($i = 0; $i -lt 15 -and -not $ready; $i++) {
    try {
        $r = Invoke-RestMethod -Uri "http://localhost:11235/health" -ErrorAction Stop
        Write-Host ($r | ConvertTo-Json -Compress)
        $ready = $true
    } catch { Start-Sleep -Seconds 2 }
}
if (-not $ready) { Write-Warning "crawl4ai did not become healthy in time." }
```

---

## Step 2 — Run the crawl

### Claude Code: use the Bash tool

Full re-crawl (all 111 pages, ~2 minutes):

```bash
cd ~/.claude/skills/gds-docs-update/scripts
python crawl_site.py --output-dir ~/.claude/skills/gds-website-builder/gds-docs
```

Single section only:

```bash
python crawl_site.py --section components  --output-dir ~/.claude/skills/gds-website-builder/gds-docs
python crawl_site.py --section patterns    --output-dir ~/.claude/skills/gds-website-builder/gds-docs
python crawl_site.py --section styles      --output-dir ~/.claude/skills/gds-website-builder/gds-docs
python crawl_site.py --section get-started --output-dir ~/.claude/skills/gds-website-builder/gds-docs
python crawl_site.py --section community   --output-dir ~/.claude/skills/gds-website-builder/gds-docs
python crawl_site.py --section accessibility --output-dir ~/.claude/skills/gds-website-builder/gds-docs
python crawl_site.py --section root        --output-dir ~/.claude/skills/gds-website-builder/gds-docs
```

Check for new/removed pages without crawling:

```bash
python crawl_site.py --sync --dry-run --output-dir ~/.claude/skills/gds-website-builder/gds-docs
```

> **Windows:** replace `~` with `%USERPROFILE%` in all paths above, or use the PowerShell commands below.

### Cowork / Claude.ai: provide these PowerShell commands to the user

```powershell
cd "$env:USERPROFILE\.claude\skills\gds-docs-update\scripts"

# Full re-crawl
python crawl_site.py --output-dir "$env:USERPROFILE\.claude\skills\gds-website-builder\gds-docs"

# Or single section
python crawl_site.py --section components --output-dir "$env:USERPROFILE\.claude\skills\gds-website-builder\gds-docs"
```

---

## Scripts reference

| Script | Purpose |
|---|---|
| `crawl_site.py` | Main crawl script. Accepts `--output-dir`, `--section`, `--dry-run`, `--sync`. |
| `site_pages.py` | Master list of all 111 page URLs, organised by section. |
| `process_md.py` | Standalone markdown cleaner — reads JSON from stdin. One-off use. |
| `save_toplevel.py` | Legacy script. Superseded by `crawl_site.py`. |

---

## Adding a new page to the site

1. Edit `site_pages.py` — add the new URL to the appropriate section in the `PAGES` dict.
2. Run `crawl_site.py` (or with `--section`) to fetch it.

---

## Workflow after a docs refresh

After re-crawling, update the gds-website-builder skill if govuk-frontend has changed:

1. Run `crawl_site.py` to get the latest docs into `gds-website-builder/gds-docs/`.
2. Review `gds-docs/community/whats-new.md` for release notes.
3. Check `gds-docs/get-started/production.md` for version changes.
4. Update `gds-website-builder/SKILL.md` if the version number or any breaking changes need updating.

---

## Markdown cleaning rules

The `clean_markdown()` function in `crawl_site.py`:

- Finds the last `1. [Home]` breadcrumb line and starts content after it
- Falls back to looking for `# Design your service` (homepage)
- Stops at `## Support links` (footer)
- Converts all `https://design-system.service.gov.uk/...` links to relative `./path.md` links
- Removes `[ ](#top)` back-to-top links
- Collapses 3+ consecutive blank lines to 2

---

## Output structure

Output goes into the `gds-website-builder` skill folder so it is co-located with the main skill:

```
~/.claude/skills/gds-website-builder/gds-docs/
  index.md
  sitemap.md
  cookies.md
  accessibility-statement.md
  privacy-policy.md
  contact.md
  design-system-team.md
  get-started.md
  get-started/
    prototyping.md  production.md  labels-legends-headings.md
    extending-and-modifying-components.md  focus-states.md  new-type-scale.md
  styles.md
  styles/
    page-template.md  layout.md  spacing.md  section-break.md
    typeface.md  type-scale.md  headings.md  paragraphs.md
    links.md  lists.md  font-override-classes.md  colour.md  images.md
  components.md
  components/
    accordion.md  back-link.md  breadcrumbs.md  button.md  ...  (34 components)
  patterns.md
  patterns/
    addresses.md  bank-details.md  dates.md  ...  (29 patterns)
  community.md
  community/
    upcoming-components-patterns.md  roadmap.md  whats-new.md  ...  (15 pages)
  accessibility.md
  accessibility/
    accessibility-strategy.md
```
