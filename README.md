# ScholarFlow · 研流

[简体中文](#简体中文) · [English](#english) · [日本語](#日本語) · [한국어](#한국어)

## 简体中文

ScholarFlow 是一套面向高校教师、研究生与科研团队的人工审核型 AI 科研工作流。它连接科研画像、论文检索与筛选、Zotero 归档、知识沉淀和本地 TeXstudio/LaTeX 写作。

```text
科研画像 → 论文雷达 → 精读 / 保存 / 忽略
        → Zotero → BibTeX → TeXstudio / LaTeX
        → literature-wiki（公开）+ research-profile（私有）
```

默认每周筛选5篇论文，并在保存前交给研究者判断。IMA可以作为可选知识归档端。

快速开始：对助手说 `使用 $scholar-flow 开始我的科研工作流。`

### 知识分层

- `literature-wiki/`：可分享的领域知识。
- `private/`：研究画像、未发表想法、失败尝试及审稿材料，不得提交到公开仓库。

### 安全边界

不要提交 API Key、学校账号或私人研究资料；不要绕过付费墙或传播授权受限的论文全文；AI生成的证明、引文和学术判断必须由研究者核验。

## English

ScholarFlow is a human-in-the-loop AI workflow connecting literature discovery, paper screening, Zotero, knowledge accumulation, and local TeXstudio/LaTeX. It separates shareable field knowledge from strictly private research context. Researchers retain final authority over correctness, novelty, citations, authorship, and publication.

Start with: `Use $scholar-flow to start my research workflow.`

## 日本語

ScholarFlow は、論文検索、Zotero、知識整理、ローカルの TeXstudio/LaTeX をつなぐ研究支援ワークフローです。AIが候補と根拠を整理し、研究者が「精読・保存・除外」を判断します。公開知識と非公開研究情報を明確に分離します。

## 한국어

ScholarFlow는 논문 탐색, Zotero, 지식 축적, 로컬 TeXstudio/LaTeX를 연결하는 연구 워크플로입니다. AI는 후보와 근거를 준비하고, 연구자는 정독·저장·제외를 결정합니다. 공개 지식과 비공개 연구 맥락을 분리합니다.

## Inspirations

- [research_LLM_wiki](https://github.com/jinleiphys/research_LLM_wiki): literature wiki and private research profile.
- [ai-research-skills](https://github.com/WenyuChiou/ai-research-skills): resumable state and human review gates.
- [ResearchClaw](https://github.com/ymx10086/ResearchClaw): literature discovery workflow patterns.

Independent implementation; workflow ideas are referenced rather than upstream source code being copied.

## Status

Version 0.1 includes the workflow, privacy rules, onboarding, retrieval guidance, Zotero/LaTeX handoff, and a non-destructive workspace initializer. Direct Zotero API writing and scheduled retrieval are planned.

## License

MIT
