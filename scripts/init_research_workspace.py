#!/usr/bin/env python3
"""Initialize a private/public research workspace without overwriting files."""
import argparse
from pathlib import Path

FILES = {
    "private/research-profile.md": """# Research profile

## Topics and equations

## Current projects

## Keywords

## Important authors, journals, and seed papers

## Methods of interest

## Exclusions

## Digest preferences
- Frequency: weekly
- Candidate count: 5
- Review gate: ask before saving
""",
    "private/workflow-preferences.md": """# Workflow preferences

- Reference manager: Zotero
- Writing environment: local TeXstudio
- Bibliography file:
- LaTeX build command:
- Optional archive: none
""",
    "private/run-log.md": "# Run log\n",
    "literature-wiki/index.md": "# Literature wiki\n\nShareable, source-backed field knowledge.\n",
    ".gitignore": "private/\n.env\n*.key\n",
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=Path)
    root = parser.parse_args().directory.expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)
    created, skipped = [], []
    for relative, content in FILES.items():
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists():
            skipped.append(relative)
        else:
            target.write_text(content, encoding="utf-8")
            created.append(relative)
    print(f"Workspace: {root}")
    print("Created: " + (", ".join(created) if created else "none"))
    print("Preserved existing: " + (", ".join(skipped) if skipped else "none"))

if __name__ == "__main__":
    main()
