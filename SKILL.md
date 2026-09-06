---
name: scholar-flow
description: Run a repeatable research workflow for university researchers using Zotero and local LaTeX/TeXstudio. Use when onboarding a research profile, planning research tasks, searching and screening papers, asking the researcher to choose 精读/保存/忽略, organizing public literature knowledge and private research context, exporting BibTeX, drafting LaTeX, or diagnosing compilation errors. Support optional IMA archiving without making it a dependency.
---

# ScholarFlow

Turn literature discovery into a human-reviewed Zotero-to-LaTeX workflow. Prepare choices and evidence; leave novelty, correctness, relevance, and publication decisions to the researcher.

## Start

1. Locate the research workspace. If none exists, run `scripts/init_research_workspace.py <directory>`.
2. Read `private/research-profile.md` and `private/workflow-preferences.md`.
3. If required fields are missing, ask only unanswered questions from `references/onboarding.md`. Offer options plus “其他”. Do not repeat known answers.
4. Default to Zotero plus local TeXstudio.
5. Never commit or share files under `private/`.

## Route the request

- “今天做什么”：run the daily workflow.
- “找最近论文”：run discovery and screening.
- “精读这篇”：create a structured reading note.
- “保存到 Zotero”：validate, deduplicate, then save only approved items.
- “写/改 LaTeX”“编译报错”：run the LaTeX workflow.
- “更新研究方向”：update the private profile and preserve dated history.

## Daily workflow

1. Use the profile, unfinished tasks, recent decisions, and available time to offer at most three tasks.
2. Read `references/retrieval.md`; search open sources first and record reproducible queries.
3. Deduplicate by DOI, then normalized title. Rank by topic, equation/problem, method, recency, seed-paper relationships, and exclusions.
4. Return 5 papers by default. Give title, authors, year, venue, DOI/link, short Chinese summary, relevance, access status, uncertainty, and `精读 / 保存 / 忽略` choices.
5. Stop for decisions. Never save all candidates automatically.
6. Apply decisions:
   - **精读**: separate claims, methods, assumptions, results, limitations, and connections. Never infer a proof from an abstract.
   - **保存**: follow `references/latex-zotero.md`; attach PDFs only when permitted.
   - **忽略**: record a short reason to tune future searches; do not make it permanent unless requested.
7. Update knowledge:
   - `literature-wiki/`: shareable, source-backed field knowledge.
   - `private/`: unpublished ideas, failed attempts, referee material, candid notes, decisions, and personal profile.
8. Cross-link private project notes to public literature pages without copying private content into them.

## LaTeX handoff

Read `references/latex-zotero.md`. Use Zotero as the bibliographic source of truth and a project `.bib` for TeXstudio. Inspect the project and build command, preserve classes/macros/labels/citation style, make the smallest scoped change, compile, diagnose the first meaningful error, and report unresolved warnings and claims requiring expert review.

Never silently rewrite proofs, change theorem assumptions, or replace citation keys across a project.

## Integrity, privacy, and optional IMA

- Label conjectures, proof sketches, and unverified citations.
- Require human review for correctness, novelty, authorship, submission, and final prose.
- Keep credentials in environment variables or an OS credential store, never in repository files.
- Do not scrape authenticated library pages, bypass limits, or redistribute licensed PDFs.
- Archive to IMA only when requested. Default to metadata, links, summaries, and user-authored notes; upload full text only when permitted.

## Finish

Append date, task, queries, candidates, decisions, changed files, compile result, and next action to `private/run-log.md`. End with one recommended next step and at most three choices.

