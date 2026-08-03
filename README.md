# 🚗 Automotive Research Agent

> Enterprise AI Research Pipeline for Automotive Technology

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![Status](https://img.shields.io/badge/Version-v1.2-green)
![Architecture](https://img.shields.io/badge/Architecture-Layered-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## Overview

Automotive Research Agent is an enterprise-style research assistant designed for automotive technology investigations.

It demonstrates how a modern research pipeline can be built using a modular architecture before introducing LLMs and AI Agents.

Current implementation focuses on:

- Enterprise Search Pipeline
- Intelligent Query Expansion
- Domain Quality Evaluation
- Search Result Ranking
- Markdown Report Generation
- Streamlit Dashboard

Future versions will gradually evolve into:

- Azure OpenAI
- RAG
- Multi-Agent Workflow

---

# Architecture

```text
                    +-------------------+
                    |   Streamlit UI    |
                    +---------+---------+
                              |
                              |
                    +---------v---------+
                    |    Controller     |
                    +---------+---------+
                              |
                              |
                    +---------v---------+
                    |     Workflow      |
                    +---------+---------+
                              |
                    +---------v---------+
                    |    Web Search     |
                    +---------+---------+
                              |
      +-----------+-----------+------------+-----------+
      |           |                        |           |
      |           |                        |           |
+-----v----+ +----v-----+          +-------v------+ +--v------+
| Query    | | Result   |          | Domain       | | Ranking |
| Builder  | | Parser   |          | Filter       | | Engine  |
+----------+ +----------+          +--------------+ +---------+
                              |
                              |
                         DuckDuckGo Search
```

---

# Features

## Search Engine

- DuckDuckGo Search
- Query Expansion
- Intelligent Ranking
- Domain Filtering
- Duplicate Removal

---

## Dashboard

- Streamlit UI
- Enterprise Layout
- Live Statistics
- Markdown Preview
- Export Ready

---

## Architecture

- Layered Architecture
- Controller Pattern
- Workflow Pattern
- Tool-based Design
- Easy Extension

---

# Project Structure

```text
automotive-research-agent/

│
├── app.py
│
├── backend/
│   ├── controller.py
│   └── workflow.py
│
├── ui/
│   ├── dashboard.py
│   ├── sidebar.py
│   ├── progress.py
│   ├── statistics.py
│   └── report.py
│
├── tools/
│   ├── web_search.py
│   ├── query_builder.py
│   ├── result_parser.py
│   ├── domain_filter.py
│   ├── ranking.py
│   ├── fetch_page.py
│   └── export_report.py
│
├── config/
│   └── domains.yaml
│
├── docs/
│
├── research/
│
└── tests/
```

---

# Search Pipeline

```text
User Query

      │

      ▼

Query Builder

      │

      ▼

DuckDuckGo Search

      │

      ▼

Result Parser

      │

      ▼

Domain Filter

      │

      ▼

Ranking Engine

      │

      ▼

Workflow

      │

      ▼

Markdown Report
```

---

# Roadmap

## Completed

- ✅ M1 Dashboard Foundation
- ✅ M2 Workflow Integration
- ✅ M3.1 Real DuckDuckGo Search
- ✅ M3.2 Enterprise Search Engine

---

## In Progress

- ⏳ M3.3 Content Extraction
- ⏳ M3.4 Extractive Summarization

---

## Future

- Azure OpenAI
- Azure AI Search
- Retrieval-Augmented Generation (RAG)
- Multi-Agent Workflow
- Enterprise Knowledge Base

---

# Technologies

- Python
- Streamlit
- DuckDuckGo Search
- YAML
- Markdown
- Enterprise Layered Architecture

---

# Example

Input

```
ADAS AI
```

↓

Pipeline

```
Query Builder

↓

Search

↓

Ranking

↓

Markdown Report
```

↓

Output

- Ranked search results
- Quality score
- Markdown report

---

# Screenshots

## Dashboard

*(Add your latest Streamlit screenshot here.)*

---

## Search Results

*(Add your latest search result screenshot here.)*

---

## Markdown Report

*(Add your report preview screenshot here.)*

---

# Version

Current Version

**v1.2 Enterprise Search Engine**

---

# Next Milestone

**M3.3**

Content Extraction

- Trafilatura
- BeautifulSoup
- Boilerplate Removal
- Main Content Extraction