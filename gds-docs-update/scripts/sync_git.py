"""
Clone or update the alphagov/govuk-design-system GitHub repository locally.

All work happens via git subprocess — no content passes through Claude as tokens.

The cloned repo is useful for browsing Nunjucks macros, component fixtures,
SASS source, and release history without an internet connection.

Target directory (in order of precedence):
  1. --target-dir <path>  (explicit override)
  2. Default: ../../gds-website-builder/gds_git/govuk-design-system  (relative to this script)

Options:
  --shallow   Use a shallow clone (--depth 1).  Default: OFF (full history).
              Use --shallow on first clone to save time; re-clone without it later
              if you need git history for blame/log.

Usage:
    python sync_git.py
    python sync_git.py --shallow
    python sync_git.py --target-dir D:/path/to/gds_git/govuk-design-system
"""

import os
import subprocess
import sys

REPO_URL = "https://github.com/alphagov/govuk-design-system.git"
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_DEFAULT_TARGET = os.path.join(
    _SCRIPT_DIR, "..", "..", "gds-website-builder", "gds_git", "govuk-design-system"
)


def run(cmd: list, cwd: str = None) -> int:
    """Run a subprocess, streaming output live. Returns the exit code."""
    print(f"  $ {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd)
    return result.returncode


def main():
    shallow = "--shallow" in sys.argv

    target_dir = _DEFAULT_TARGET
    if "--target-dir" in sys.argv:
        idx = sys.argv.index("--target-dir")
        target_dir = os.path.abspath(sys.argv[idx + 1])
    else:
        target_dir = os.path.abspath(target_dir)

    print(f"Target directory : {target_dir}")
    print(f"Repository URL   : {REPO_URL}")
    print(f"Shallow clone    : {shallow}")
    print()

    git_dir = os.path.join(target_dir, ".git")

    if os.path.isdir(git_dir):
        # Repo exists — pull latest
        print("Repository already exists. Pulling latest changes ...")
        rc = run(["git", "pull", "--ff-only"], cwd=target_dir)
        if rc != 0:
            print(f"\nERROR: git pull failed (exit code {rc}).")
            print("If the working tree has local changes, stash or reset them first:")
            print(f"  cd {target_dir}")
            print("  git stash")
            print("  git pull --ff-only")
            sys.exit(rc)
        print("\nDone. Repository is up to date.")

    else:
        # Repo does not exist — clone it
        print("Repository not found. Cloning ...")
        os.makedirs(os.path.dirname(target_dir), exist_ok=True)

        clone_cmd = ["git", "clone"]
        if shallow:
            clone_cmd += ["--depth", "1"]
        clone_cmd += [REPO_URL, target_dir]

        rc = run(clone_cmd)
        if rc != 0:
            print(f"\nERROR: git clone failed (exit code {rc}).")
            sys.exit(rc)
        print("\nDone. Repository cloned.")

    # Print summary of what was cloned
    print()
    if os.path.isdir(target_dir):
        top_level = sorted(os.listdir(target_dir))
        print("Top-level contents:")
        for name in top_level:
            if name != ".git":
                print(f"  {name}/")


if __name__ == "__main__":
    main()
