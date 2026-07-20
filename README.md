# Automotive Research Agent

A modular Python-based research agent that automatically searches the web, extracts the main content from webpages, generates structured summaries, and exports the results as a Markdown research report.

---

## Overview

Automotive Research Agent automates the process of collecting technical information from the Internet.

The system performs the following tasks:

- Search relevant webpages
- Filter low-quality search results
- Download webpage content
- Extract the main article text
- Generate extractive summaries
- Export a structured Markdown report

The project follows a modular architecture, making it easy to extend with AI-powered summarization, RAG, or multi-agent workflows in future versions.

---

## Features

- Web search using DDGS
- Candidate URL filtering
- Intelligent page collection
- Main content extraction using Trafilatura
- BeautifulSoup fallback for unsupported webpages
- Automatic text cleaning
- Extractive summarization
- Markdown report generation
- Modular architecture for future AI integration

---

## Architecture

```
                User
                  │
                  ▼
          Automotive Research Agent
                  │
                  ▼
             Search Engine
                  │
                  ▼
             Fetch Engine
      (Trafilatura + BS4 Fallback)
                  │
                  ▼
            Summary Engine
                  │
                  ▼
            Markdown Report
```

---

## Workflow

```
User Input
      │
      ▼
web_search.py
      │
      ▼
fetch_page.py
      │
      ▼
summarize.py
      │
      ▼
export_report.py
      │
      ▼
report.md
```

---

## Project Structure

```
automotive-research-agent/
│
├── docs/
│
├── research/
│   ├── cache/
│   └── final/
│
├── tools/
│   ├── web_search.py
│   ├── fetch_page.py
│   ├── summarize.py
│   ├── export_report.py
│   └── read_pdf.py
│
├── agent.py
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Components

### web_search.py

Responsible for:

- Search webpages
- Filter unwanted domains
- Return candidate URLs

---

### fetch_page.py

Responsible for:

- Download HTML
- Extract webpage content
- Trafilatura extraction
- BeautifulSoup fallback
- Text cleaning
- Cache downloaded content

---

### summarize.py

Responsible for:

- Generate extractive summaries
- Preserve page title
- Preserve source URL

---

### export_report.py

Responsible for:

- Generate Markdown reports
- Format research results

---

### agent.py

Coordinates the complete research workflow.

---

## Installation

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

## Dependencies

Core libraries:

- requests
- beautifulsoup4
- trafilatura
- ddgs

---

## Usage

Run the application

```bash
python main.py
```

Example

```
Enter research topic:

ADAS AI
```

---

## Example Output

```
Research Report

Topic

ADAS AI

--------------------------------

Source 1

Title

AI Technologies for ADAS Systems

Summary

ADAS systems combine computer vision,
sensor fusion and AI algorithms to
assist drivers and improve road safety.

URL

https://...
```

---

## Current Version

**Version: v1.0**

### Implemented

- DDGS web search
- URL filtering
- Candidate URL collection
- Intelligent page collection
- Trafilatura content extraction
- BeautifulSoup fallback
- Text cleaning
- Extractive summary
- Markdown report generation
- Modular architecture

---

## Roadmap

### Prototype

- Web Search
- BeautifulSoup Extraction
- Raw Report

---

### v1.0 (Current)

- Modular Research Pipeline
- Intelligent Search Strategy
- Content Extraction
- Extractive Summary
- Markdown Report

---

### v2.0

- Azure OpenAI Summary
- AI-generated research report

---

### v3.0

- RAG
- Vector Database
- Multi-source Retrieval
- Agent Memory

---

## Future Improvements

- PDF content extraction
- Search result ranking
- Better extractive summarization
- Azure OpenAI integration
- Multi-agent collaboration
- Web UI
- REST API

---

## License

This project is intended for educational and learning purposes.