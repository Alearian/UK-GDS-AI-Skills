#!/usr/bin/env bash
# install.sh — Install GDS AI Skills
# Usage: bash install.sh [--tool <tool>] [--skills-dir <path>]
#
# Tools: claude-code (default), cursor, copilot, windsurf, all

set -e

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="${HOME}/.claude/skills"
TOOL="claude-code"

# Parse arguments
while [[ $# -gt 0 ]]; do
  case $1 in
    --tool) TOOL="$2"; shift 2 ;;
    --skills-dir) SKILLS_DIR="$2"; shift 2 ;;
    *) echo "Unknown option: $1"; exit 1 ;;
  esac
done

echo "GDS AI Skills Installer"
echo "========================"
echo "Tool:       $TOOL"
echo "Repo:       $REPO_DIR"

install_claude_code() {
  echo ""
  echo "Installing for Claude Code..."
  mkdir -p "$SKILLS_DIR"
  cp -r "$REPO_DIR/gds-website-builder" "$SKILLS_DIR/"
  cp -r "$REPO_DIR/gds-docs-update"    "$SKILLS_DIR/"
  echo "  Copied gds-website-builder → $SKILLS_DIR/gds-website-builder"
  echo "  Copied gds-docs-update     → $SKILLS_DIR/gds-docs-update"
  echo ""
  echo "Done. Restart Claude Code to load the skills."
}

install_cursor() {
  echo ""
  echo "Installing for Cursor..."
  PROJECT_DIR="${1:-$(pwd)}"
  mkdir -p "$PROJECT_DIR/.cursor/rules"
  cp "$REPO_DIR/gds-website-builder/adapters/cursor.mdc" \
     "$PROJECT_DIR/.cursor/rules/gds-website-builder.mdc"
  echo "  Copied cursor.mdc → $PROJECT_DIR/.cursor/rules/gds-website-builder.mdc"
  echo ""
  echo "  To use the full component docs, also copy the gds-docs folder:"
  echo "    cp -r $REPO_DIR/gds-website-builder/gds-docs $PROJECT_DIR/"
  echo ""
  echo "Done. The rule will activate automatically in Cursor for GDS-related prompts."
}

install_copilot() {
  echo ""
  echo "Installing for GitHub Copilot..."
  PROJECT_DIR="${1:-$(pwd)}"
  mkdir -p "$PROJECT_DIR/.github"
  cp "$REPO_DIR/gds-website-builder/adapters/copilot-instructions.md" \
     "$PROJECT_DIR/.github/copilot-instructions.md"
  echo "  Copied copilot-instructions.md → $PROJECT_DIR/.github/copilot-instructions.md"
  echo ""
  echo "  To use the full component docs, also copy the gds-docs folder:"
  echo "    cp -r $REPO_DIR/gds-website-builder/gds-docs $PROJECT_DIR/"
  echo ""
  echo "Done. Copilot will load these instructions automatically for this project."
}

install_windsurf() {
  echo ""
  echo "Installing for Windsurf..."
  PROJECT_DIR="${1:-$(pwd)}"
  cp "$REPO_DIR/gds-website-builder/adapters/windsurf.rules" \
     "$PROJECT_DIR/.windsurfrules"
  echo "  Copied windsurf.rules → $PROJECT_DIR/.windsurfrules"
  echo ""
  echo "  To use the full component docs, also copy the gds-docs folder:"
  echo "    cp -r $REPO_DIR/gds-website-builder/gds-docs $PROJECT_DIR/"
  echo ""
  echo "Done. Windsurf will load these rules automatically for this project."
}

case "$TOOL" in
  claude-code) install_claude_code ;;
  cursor)      install_cursor ;;
  copilot)     install_copilot ;;
  windsurf)    install_windsurf ;;
  all)
    install_claude_code
    install_cursor
    install_copilot
    install_windsurf
    ;;
  *)
    echo "Unknown tool: $TOOL"
    echo "Valid options: claude-code, cursor, copilot, windsurf, all"
    exit 1
    ;;
esac
