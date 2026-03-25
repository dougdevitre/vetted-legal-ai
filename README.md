# 🤖 Vetted Legal AI Engine

**Fix the reliability gap.**

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/dougdevitre/vetted-legal-ai/pulls)

---

## The Problem

General-purpose AI models hallucinate legal citations, fabricate case law, and produce unreliable advice. When an attorney submits a brief with fake citations, courts sanction them. When a self-represented litigant follows bad AI advice, they lose their case.

The reliability gap in legal AI is not a minor inconvenience — it is a liability risk that undermines trust in the entire system.

## The Solution

A Retrieval-Augmented Generation (RAG) engine purpose-built for legal applications. Every response is grounded in verified legal data. Every citation is validated against its source. Every answer carries a confidence score. Every query leaves a complete audit trail.

This is not a chatbot with a legal skin. It is infrastructure for trustworthy legal AI.

---

## Architecture

```mermaid
graph LR
    Q[User Query] --> EMB[Embedding]
    EMB --> VS[Vector Search]
    VS --> CA[Context Assembly]
    CA --> LLM[LLM Generation]
    LLM --> CV[Citation Validator]
    CV --> CS[Confidence Scorer]
    CS --> AL[Audit Logger]
    AL --> R[Verified Response]

    subgraph RAG Pipeline
        EMB
        VS
        CA
    end

    subgraph Validation Layer
        CV
        CS
        AL
    end
```

---

## Who This Helps

| Audience | How This Helps |
|---|---|
| **Legal aid organizations** | Reliable AI assistance without hallucination risk |
| **Pro bono attorneys** | Research tool they can trust for real case work |
| **Court self-help centers** | Provide accurate, sourced information to litigants |
| **Justice tech platforms** | Embed vetted AI into their applications |

---

## Features

- [ ] RAG pipeline with verified legal corpus
- [ ] Citation validation — every citation checked against source material
- [ ] Confidence scoring per response (high / medium / low / insufficient)
- [ ] Complete audit trail — query, sources, generation, validation logged
- [ ] Jurisdiction-aware retrieval — filter by state, federal, or topic
- [ ] Source transparency — full provenance chain for every answer
- [ ] Pluggable LLM backend (OpenAI, Anthropic, local models)
- [ ] FastAPI-based REST interface

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11+ |
| RAG Framework | LangChain |
| Vector Store | ChromaDB |
| API | FastAPI |
| Validation | Pydantic |
| Testing | pytest |
| Linting | Ruff + mypy |

---

## Quick Start

```bash
git clone https://github.com/dougdevitre/vetted-legal-ai.git
cd vetted-legal-ai
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
uvicorn src.vetted_legal_ai.api.routes:app --reload
```

---

## Justice OS Ecosystem

| Repo | Description |
|---|---|
| [justice-os](https://github.com/dougdevitre/justice-os) | Core modular platform |
| [mobile-court-access](https://github.com/dougdevitre/mobile-court-access) | Mobile-first court access kit |
| [vetted-legal-ai](https://github.com/dougdevitre/vetted-legal-ai) | RAG engine with citation validation (you are here) |
| [court-doc-engine](https://github.com/dougdevitre/court-doc-engine) | Document automation for legal filings |

---

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT — see [LICENSE](LICENSE).
