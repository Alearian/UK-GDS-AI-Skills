# install.ps1 — Install GDS AI Skills (Windows)
# Usage: .\install.ps1 [-Tool <tool>] [-ProjectDir <path>]
#
# Tools: claude-code (default), cursor, copilot, windsurf, all

param(
  [string]$Tool       = "claude-code",
  [string]$ProjectDir = (Get-Location).Path
)

$RepoDir   = $PSScriptRoot
$SkillsDir = "$env:USERPROFILE\.claude\skills"

Write-Host "GDS AI Skills Installer" -ForegroundColor Cyan
Write-Host "========================" -ForegroundColor Cyan
Write-Host "Tool:       $Tool"
Write-Host "Repo:       $RepoDir"

function Install-ClaudeCode {
  Write-Host ""
  Write-Host "Installing for Claude Code..." -ForegroundColor Green
  New-Item -ItemType Directory -Force -Path $SkillsDir | Out-Null
  Copy-Item -Recurse -Force "$RepoDir\gds-website-builder" "$SkillsDir\"
  Copy-Item -Recurse -Force "$RepoDir\gds-docs-update"    "$SkillsDir\"
  Write-Host "  Copied gds-website-builder -> $SkillsDir\gds-website-builder"
  Write-Host "  Copied gds-docs-update     -> $SkillsDir\gds-docs-update"
  Write-Host ""
  Write-Host "Done. Restart Claude Code to load the skills." -ForegroundColor Green
}

function Install-Cursor {
  Write-Host ""
  Write-Host "Installing for Cursor..." -ForegroundColor Green
  New-Item -ItemType Directory -Force -Path "$ProjectDir\.cursor\rules" | Out-Null
  Copy-Item -Force "$RepoDir\gds-website-builder\adapters\cursor.mdc" `
                   "$ProjectDir\.cursor\rules\gds-website-builder.mdc"
  Write-Host "  Copied cursor.mdc -> $ProjectDir\.cursor\rules\gds-website-builder.mdc"
  Write-Host ""
  Write-Host "  To use the full component docs, also copy the gds-docs folder:"
  Write-Host "    Copy-Item -Recurse $RepoDir\gds-website-builder\gds-docs $ProjectDir\"
  Write-Host ""
  Write-Host "Done. The rule will activate automatically in Cursor for GDS-related prompts." -ForegroundColor Green
}

function Install-Copilot {
  Write-Host ""
  Write-Host "Installing for GitHub Copilot..." -ForegroundColor Green
  New-Item -ItemType Directory -Force -Path "$ProjectDir\.github" | Out-Null
  Copy-Item -Force "$RepoDir\gds-website-builder\adapters\copilot-instructions.md" `
                   "$ProjectDir\.github\copilot-instructions.md"
  Write-Host "  Copied copilot-instructions.md -> $ProjectDir\.github\copilot-instructions.md"
  Write-Host ""
  Write-Host "  To use the full component docs, also copy the gds-docs folder:"
  Write-Host "    Copy-Item -Recurse $RepoDir\gds-website-builder\gds-docs $ProjectDir\"
  Write-Host ""
  Write-Host "Done. Copilot will load these instructions automatically for this project." -ForegroundColor Green
}

function Install-Windsurf {
  Write-Host ""
  Write-Host "Installing for Windsurf..." -ForegroundColor Green
  Copy-Item -Force "$RepoDir\gds-website-builder\adapters\windsurf.rules" `
                   "$ProjectDir\.windsurfrules"
  Write-Host "  Copied windsurf.rules -> $ProjectDir\.windsurfrules"
  Write-Host ""
  Write-Host "  To use the full component docs, also copy the gds-docs folder:"
  Write-Host "    Copy-Item -Recurse $RepoDir\gds-website-builder\gds-docs $ProjectDir\"
  Write-Host ""
  Write-Host "Done. Windsurf will load these rules automatically for this project." -ForegroundColor Green
}

switch ($Tool) {
  "claude-code" { Install-ClaudeCode }
  "cursor"      { Install-Cursor }
  "copilot"     { Install-Copilot }
  "windsurf"    { Install-Windsurf }
  "all"         { Install-ClaudeCode; Install-Cursor; Install-Copilot; Install-Windsurf }
  default {
    Write-Host "Unknown tool: $Tool" -ForegroundColor Red
    Write-Host "Valid options: claude-code, cursor, copilot, windsurf, all"
    exit 1
  }
}
