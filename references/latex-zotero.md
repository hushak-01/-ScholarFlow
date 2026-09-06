# Zotero and local TeXstudio

Zotero is the bibliographic source of truth; the project `.bib` supplies citations; TeXstudio edits and builds the manuscript.

## Save an approved paper

1. Match DOI; otherwise normalized title and first author.
2. Verify title, author order, year, venue, DOI, and item type.
3. Add approved topic tags and one reading-status tag.
4. Preserve stable citation keys. If Better BibTeX exists, preserve its key and export settings.
5. Attach a PDF only when storage rights permit it.

## Build and diagnose

Detect the existing build method: commonly `latexmk`, `pdflatex + bibtex`, or `pdflatex + biber`. Respect `% !TeX program` and project configuration. Compile without destructive cleanup; diagnose the first root error before cascade messages; check missing files, undefined commands, environment mismatch, labels, citation backend, and encoding; recompile enough times for references to settle.

Reuse existing notation and macros. Cite only verified entries. Mark unsupported claims `TODO: verify source`. Present proof edits as reviewable patches and list assumptions added or removed.
