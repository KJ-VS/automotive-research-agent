# 🚗 Automotive Research Agent

Enterprise AI Research Platform for intelligent automotive technology research.

The project automates the complete research workflow from web search to report generation using a modular and extensible architecture.

---

# Current Version

**V1.3 – Enterprise Research Pipeline**

---

# Features

## Search

- DuckDuckGo Search
- Intelligent Query Builder
- Domain Filtering
- Configurable Ranking
- Duplicate URL Removal

---

## Content Extraction

- HTML Download
- Trafilatura Extraction
- BeautifulSoup Fallback
- Content Cleaning
- Local Cache

---

## Summarization

- Extractive Summarization
- Sentence Filtering
- Clean Markdown Output

---

## Analytics

- Research Statistics
- Search Analytics
- Average Overall Score
- Top Score
- Best Domain
- Average Domain Score
- Average Content Length

---

## Report

- Markdown Report Export
- Overall Score
- Ranked Search Results
- Detailed Research Results
- Streamlit Report Preview

---

## Dashboard

- Enterprise Dashboard
- Research Statistics
- Search Analytics
- Report Preview
- Sidebar Configuration

---

# Workflow

```text
Research Question
        │
        ▼
Web Search
        │
        ▼
Domain Filter
        │
        ▼
Ranking
        │
        ▼
Content Extraction
        │
        ▼
Summarization
        │
        ▼
Analytics
        │
        ▼
Markdown Report
        │
        ▼
Dashboard
```

---

# Project Structure

```text
automotive-research-agent/

├── app.py
│
├── backend/
│   ├── controller.py
│   └── workflow.py
│
├── config/
│   ├── config.yaml
│   ├── domains.yaml
│   └── ranking.yaml
│
├── tools/
│   ├── analytics.py
│   ├── domain_filter.py
│   ├── export_report.py
│   ├── fetch_page.py
│   ├── query_builder.py
│   ├── ranking.py
│   ├── read_pdf.py
│   ├── result_parser.py
│   ├── summarize.py
│   └── web_search.py
│
├── ui/
│   ├── dashboard.py
│   ├── progress.py
│   ├── report.py
│   ├── sidebar.py
│   └── statistics.py
│
├── research/
│   ├── cache/
│   └── final/
│
├── README.md
└── CHANGELOG.md
```

---

# Dashboard

The Streamlit dashboard provides:

- Research Question
- Research Status
- Research Statistics
- Search Analytics
- Markdown Report Preview

---

# Analytics

The Analytics Engine automatically generates:

- Average Overall Score
- Top Score
- Best Domain
- Average Domain Score
- Average Content Length

---

# Report

The generated Markdown report contains:

- Topic
- Retrieved Pages
- Detailed Research Results
- Overall Score
- Summary
- Ranked Search Results

---

# Technology Stack

- Python 3
- Streamlit
- DuckDuckGo Search (DDGS)
- Trafilatura
- BeautifulSoup4
- Requests
- PyYAML

---

# Future Roadmap

## V1.3.1

- Executive Summary
- Improved Report Layout
- Expandable Detailed Results
- Enterprise Report Design

## V1.4

- Multiple Search Engines
- Search Provider Abstraction
- Tavily Support
- SerpAPI Support

## V2.0

- LLM-based Summarization
- AI Report Generation

## V3.0

- RAG Knowledge Base
- Conversational Research Assistant

---

# Author

Automotive Research Agent

Enterprise AI Research Platform

Version **V1.3**