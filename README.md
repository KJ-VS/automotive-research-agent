# Automotive Research Agent

A Python-based research agent that searches the web, downloads relevant web pages, and generates structured research reports.

This project is developed as part of an Automotive AI training project. The first version does **not** use any Large Language Model (LLM). The entire workflow is controlled by Python logic.

---

# Version

Current Version

```
v0.1
```

Status

```
Project Structure Completed
```

---

# Features

Current Features

- Python-based workflow
- Modular architecture
- Web search
- Web page fetching
- Local cache
- Markdown report generation

Future Features

- Read local PDF documents
- Combine local documents with web search results
- AI planning
- Azure OpenAI integration
- Docker deployment

---

# Project Structure

```text
automotive-research-agent
│
├── main.py
├── agent.py
│
├── tools/
│   ├── web_search.py
│   ├── fetch_page.py
│   ├── read_pdf.py
│   └── export_report.py
│
├── docs/
│
├── research/
│   ├── cache/
│   └── final/
│
├── requirements.txt
└── README.md
```

---

# Architecture

## main.py

Application entry point.

Responsibilities

- Start the application
- Receive the research topic
- Create the ResearchAgent
- Start the workflow

---

## agent.py

Workflow controller.

Responsibilities

- Coordinate the complete workflow
- Call different tools
- Manage the execution order
- Finish the research process

Workflow

```text
User Input
      │
      ▼
Web Search
      │
      ▼
Fetch Web Pages
      │
      ▼
Generate Report
      │
      ▼
Finish
```

---

## tools/web_search.py

Searches the web.

Input

```
Research Topic
```

Output

```
List of URLs
```

---

## tools/fetch_page.py

Downloads the web page content.

Downloaded pages are stored inside

```
research/cache/
```

---

## tools/export_report.py

Generates the final Markdown report.

Output

```
research/final/report.md
```

---

## docs/

Reserved for local documents.

Examples

```
AUTOSAR.pdf
UNECE-R155.pdf
ISO26262.pdf
```

Not used in Version 1.

---

## research/cache/

Temporary storage for downloaded web pages.

Example

```
page1.txt
page2.txt
page3.txt
```

---

## research/final/

Stores the final research report.

Example

```
report.md
```

---

# Workflow

```text
User
 │
 ▼
main.py
 │
 ▼
agent.py
 │
 ├───────────────┐
 │               │
 ▼               ▼
web_search.py   read_pdf.py (Future)
 │
 ▼
fetch_page.py
 │
 ▼
research/cache/
 │
 ▼
export_report.py
 │
 ▼
research/final/report.md
 │
 ▼
End
```

---

# Python Workflow

The first version is implemented without any LLM.

Workflow

```
User Input
      │
      ▼
Python Logic
      │
      ▼
Search
      │
      ▼
Fetch
      │
      ▼
Export Report
```

Future versions may replace the Python workflow controller with an AI Agent powered by Azure OpenAI.

---

# Requirements

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Run

Run the application

```bash
python main.py
```

---

# Roadmap

Version 0.1

- Project structure
- Git repository
- Basic workflow

Version 0.2

- Implement main.py

Version 0.3

- Implement ResearchAgent

Version 0.4

- Implement web search

Version 0.5

- Implement page fetching

Version 0.6

- Generate Markdown report

Version 1.0

- Complete working demo

---

# License

This project is created for learning and demonstration purposes.