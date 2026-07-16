# Automotive Research Agent — Architecture

## System Flow Diagram

```mermaid
flowchart TD
    subgraph Input
        USER["👤 User"]
        TOPIC["📝 Research Topic"]
    end

    subgraph Entry Point
        MAIN["main.py<br/>Entry Point"]
    end

    subgraph Orchestrator
        AGENT["agent.py<br/>ResearchAgent.run()"]
    end

    subgraph Tools["tools/ Package"]
        WS["web_search.py<br/>🔍 Web Search"]
        FP["fetch_page.py<br/>📥 Fetch Pages"]
        RP["read_pdf.py<br/>📄 Read PDFs"]
        ER["export_report.py<br/>📊 Export Report"]
    end

    subgraph Storage
        CACHE["research/cache/<br/>💾 Local Cache"]
        FINAL["research/final/<br/>📁 Final Reports"]
    end

    subgraph External
        WEB["🌐 Internet<br/>Search Engines / Web Pages"]
        PDF["📂 Local PDF<br/>Documents"]
    end

    USER -->|"Enter topic"| MAIN
    MAIN -->|"agent.run(topic)"| AGENT
    AGENT -->|"1. Search"| WS
    AGENT -->|"2. Fetch"| FP
    AGENT -->|"3. Read PDFs (future)"| RP
    AGENT -->|"4. Export"| ER

    WS -->|"Query"| WEB
    WEB -->|"Search Results"| WS

    FP -->|"Download"| WEB
    WEB -->|"Page Content"| FP
    FP -->|"Cache pages"| CACHE

    RP -->|"Read"| PDF
    PDF -->|"Extracted Text"| RP

    ER -->|"Write report"| FINAL
```

## Component Diagram

```mermaid
graph LR
    subgraph "Automotive Research Agent"
        direction TB
        A[main.py] --> B[agent.py]
        B --> C[tools/web_search.py]
        B --> D[tools/fetch_page.py]
        B --> E[tools/read_pdf.py]
        B --> F[tools/export_report.py]
    end

    C --> G[(research/cache)]
    D --> G
    F --> H[(research/final)]
```

## Data Flow

```mermaid
sequenceDiagram
    actor User
    participant main.py
    participant ResearchAgent
    participant web_search
    participant fetch_page
    participant export_report
    participant Cache as research/cache
    participant Output as research/final

    User->>main.py: Enter research topic
    main.py->>ResearchAgent: run(topic)
    ResearchAgent->>web_search: web_search(topic)
    web_search-->>ResearchAgent: search_results
    ResearchAgent->>fetch_page: fetch_page(search_results)
    fetch_page->>Cache: Store downloaded pages
    fetch_page-->>ResearchAgent: pages
    ResearchAgent->>export_report: export_report(topic, pages)
    export_report->>Output: Write Markdown report
    export_report-->>ResearchAgent: Done
    ResearchAgent-->>User: Report generated
```

## Directory Structure

```
automotive-research-agent/
├── main.py                 # Entry point — CLI interface
├── agent.py                # Orchestrator — workflow logic
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Git ignore rules
├── docs/
│   ├── .gitkeep
│   └── architecture.md     # Architecture diagrams (this file)
├── tools/
│   ├── __init__.py         # (to be created)
│   ├── web_search.py       # Web search tool
│   ├── fetch_page.py       # Page fetching tool
│   ├── read_pdf.py         # PDF reading tool
│   └── export_report.py    # Report generation tool
└── research/
    ├── cache/              # Cached web page downloads
    └── final/              # Generated research reports
```

## Implementation Status

| Component | v0.1 | v0.2 | v1.0 |
|---|---|---|---|
| `main.py` | ✅ | ✅ | ✅ |
| `agent.py` | ✅ | ✅ | ✅ |
| `web_search.py` | ❌ | ✅ | ✅ |
| `fetch_page.py` | ❌ | ✅ | ✅ |
| `read_pdf.py` | ❌ | ❌ | ✅ |
| `export_report.py` | ❌ | ✅ | ✅ |
| LLM Integration | ❌ | ❌ | ❌ (future) |
| Docker | ❌ | ❌ | ❌ (future) |