# 🚗 Automotive Research Agent

An enterprise-oriented research platform for automotive technology research.

The project started as a rule-based research pipeline and is gradually evolving into an enterprise AI research platform with Web UI, LLM, RAG, and Multi-Agent capabilities.

---

# Current Status

**Current Version**

🚧 **V1.1 (In Development)**

Latest completed milestone:

- Project refactoring
- Modular architecture
- Streamlit dashboard prototype
- Backend / UI separation
- YAML configuration

---

# Roadmap

| Version | Status | Description |
|----------|--------|-------------|
| Prototype | ✅ Completed | Initial research prototype |
| V1.0 | ✅ Released | Rule-based CLI research engine |
| V1.1 | 🚧 In Development | Web dashboard & modular architecture |
| V2.0 | ⏳ Planned | LLM-powered research assistant |
| V3.0 | ⏳ Planned | Enterprise RAG platform |
| V4.0 | ⏳ Planned | Multi-Agent AI research platform |

---

# Overview

Automotive Research Agent automates the process of collecting technical information from the Internet.

The system performs the following tasks:

- Search relevant webpages
- Filter low-quality search results
- Download webpage content
- Extract the main article
- Generate structured summaries
- Export research reports

The project is designed with a modular architecture to support future AI capabilities such as:

- Azure OpenAI
- RAG
- Enterprise Knowledge Base
- Multi-Agent Workflow

---

# Features

## V1.0

- Rule-based web search
- Candidate URL filtering
- Intelligent webpage collection
- Trafilatura content extraction
- BeautifulSoup fallback
- Extractive summarization
- Markdown report generation

## V1.1

- Streamlit dashboard
- Modular backend architecture
- Configuration management
- Web UI prototype

---

# System Architecture

```
                  Browser / CLI
                       │
                       ▼
         Automotive Research Dashboard
                       │
                       ▼
                  Controller
                       │
                       ▼
                    Workflow
                       │
                       ▼
                Research Agent
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
     Search         Fetch         Summary
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                  Markdown Report
```

---

# Project Structure

```text
automotive-research-agent/

├── backend/
│   ├── agent.py
│   ├── controller.py
│   ├── workflow.py
│   └── config.py
│
├── config/
│   ├── config.yaml
│   └── domains.yaml
│
├── docs/
│   ├── architecture.md
│   └── architecture.svg
│
├── logs/
│
├── research/
│
├── tests/
│
├── tools/
│
├── ui/
│   ├── dashboard.py
│   ├── sidebar.py
│   ├── progress.py
│   ├── statistics.py
│   └── report.py
│
├── app.py
├── main.py
├── README.md
├── CHANGELOG.md
├── requirements.txt
└── .gitignore
```

---

# Components

## backend

Responsible for coordinating the complete research workflow.

- Agent
- Controller
- Workflow
- Configuration

---

## tools

Provides reusable tools including:

- Web search
- Content extraction
- Summarization
- Report generation

---

## ui

Responsible for the Streamlit dashboard.

- Dashboard
- Sidebar
- Progress
- Statistics
- Report Preview

---

## config

Stores project configuration.

- Search settings
- Domain filtering
- Future LLM configuration

---

# Installation

Clone the repository

```bash
git clone https://github.com/<your-account>/automotive-research-agent.git

cd automotive-research-agent
```

Create virtual environment

```bash
python -m venv .venv
```

Activate virtual environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Quick Start

## CLI Version

```bash
python main.py
```

## Web Dashboard

```bash
streamlit run app.py
```

---

# Dependencies

Core libraries

- requests
- beautifulsoup4
- trafilatura
- ddgs
- streamlit

---

# Current Development

V1.1 currently focuses on building the software architecture rather than AI capabilities.

Current milestones include:

- Repository refactoring
- Streamlit dashboard
- UI modularization
- Controller integration
- Workflow orchestration

---

# Future Versions

## V2

- Azure OpenAI integration
- AI-generated summaries
- Interactive report generation

---

## V3

- RAG
- Vector database
- Enterprise knowledge retrieval
- Multi-source search

---

## V4

- Multi-Agent orchestration
- Planner Agent
- Search Agent
- Summary Agent
- Report Agent
- Enterprise AI Platform

---

# Changelog

See **CHANGELOG.md** for detailed version history.

---

# License

This project is intended for educational and learning purposes.