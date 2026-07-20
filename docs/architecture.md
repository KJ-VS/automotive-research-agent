# Automotive Research Agent — Architecture

## Overview

The Automotive Research Agent is a modular Python application designed to automate technical research workflows.

Current workflow:

1. Search candidate URLs
2. Download and extract web page content
3. Generate extractive summaries
4. Export a Markdown research report

The modular architecture enables future extensions such as:

- Azure OpenAI
- RAG (Retrieval-Augmented Generation)
- PDF document processing
- Multi-Agent workflows

---

## System Flow Diagram

```mermaid
flowchart TD

    subgraph Input
        USER["👤 User"]
        TOPIC["📝 Research Topic"]
    end

    subgraph EntryPoint
        MAIN["main.py<br/>Entry Point"]
    end

    subgraph Orchestrator
        AGENT["agent.py<br/>ResearchAgent.run()"]
    end

    subgraph Tools["tools/ Package"]
        WS["🔍 Search Engine<br/>web_search.py"]
        FP["📥 Fetch Engine<br/>fetch_page.py"]
        SM["📝 Summary Engine<br/>summarize.py"]
        RP["📄 PDF Reader (Future)<br/>read_pdf.py"]
        ER["📊 Report Engine<br/>export_report.py"]
    end

    subgraph Storage
        CACHE["💾 research/cache"]
        FINAL["📁 research/final"]
    end

    subgraph External
        WEB["🌐 Internet"]
        PDF["📄 Local PDFs"]
    end

    USER --> MAIN
    MAIN --> AGENT

    AGENT --> WS
    WS --> WEB
    WEB --> WS

    WS --> FP
    FP --> WEB
    WEB --> FP

    FP --> CACHE

    FP --> SM
    SM --> ER

    AGENT -. Future .-> RP
    RP --> PDF

    ER --> FINAL
```

---

## Component Diagram

```mermaid
graph LR

subgraph Automotive_Research_Agent

direction TB

MAIN[main.py]

AGENT[agent.py]

SEARCH[web_search.py]

FETCH[fetch_page.py]

SUMMARY[summarize.py]

PDF[read_pdf.py]

REPORT[export_report.py]

MAIN --> AGENT

AGENT --> SEARCH

SEARCH --> FETCH

FETCH --> SUMMARY

SUMMARY --> REPORT

AGENT -. Future .-> PDF

end

FETCH --> CACHE[(research/cache)]

REPORT --> FINAL[(research/final)]
```

---

## Data Flow

```mermaid
sequenceDiagram

actor User

participant Main as main.py

participant Agent as ResearchAgent

participant Search as web_search

participant Fetch as fetch_page

participant Summary as summarize

participant Report as export_report

participant Cache as research/cache

participant Output as research/final

User->>Main: Enter topic

Main->>Agent: run(topic)

Agent->>Search: Search URLs

Search-->>Agent: Candidate URLs

Agent->>Fetch: Download pages

Fetch->>Cache: Save cache

Fetch-->>Agent: Extracted pages

Agent->>Summary: Generate summaries

Summary-->>Agent: Summaries

Agent->>Report: Export report

Report->>Output: report.md

Report-->>Agent: Completed

Agent-->>User: Report generated
```

---

## Directory Structure

```text
automotive-research-agent/
│
├── main.py
├── agent.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── docs/
│   ├── architecture.md
│   └── architecture.svg
│
├── tools/
│   ├── web_search.py
│   ├── fetch_page.py
│   ├── summarize.py
│   ├── read_pdf.py
│   └── export_report.py
│
└── research/
    ├── cache/
    │   └── .gitkeep
    └── final/
        └── .gitkeep
```

---

## Current Workflow

```text
User
   │
   ▼
main.py
   │
   ▼
ResearchAgent
   │
   ▼
Search Engine
   │
   ▼
Fetch Engine
   │
   ▼
Summary Engine
   │
   ▼
Report Engine
   │
   ▼
Markdown Report
```

---

## Implementation Status

| Component | Status |
|-----------|--------|
| main.py | ✅ |
| agent.py | ✅ |
| web_search.py | ✅ |
| fetch_page.py | ✅ |
| summarize.py | ✅ |
| export_report.py | ✅ |
| read_pdf.py | 🚧 Planned |
| Azure OpenAI | 🚧 Future |
| RAG | 🚧 Future |
| Multi-Agent | 🚧 Future |
| Docker | 🚧 Future |

---

## Future Roadmap

### v1.1

- Retry mechanism
- Logging
- Better error handling

### v2.0

- Azure OpenAI integration
- AI-generated summaries

### v3.0

- Vector Database
- RAG
- Semantic Search

### v4.0

- Multi-Agent Workflow
- Planning Agent
- Retrieval Agent
- Report Agent