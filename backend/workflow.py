"""
Workflow Layer

Coordinates the complete research pipeline.

Version
-------
M3.3 Final

Pipeline
--------
Search
    ↓
Content Extraction
    ↓
Summarization
    ↓
Report Export
"""

import time

from tools.web_search import WebSearch
from tools.fetch_page import FetchPage
from tools.summarize import Summarizer
from tools.export_report import ReportExporter


class Workflow:
    """
    Enterprise Workflow Coordinator.
    """

    def __init__(self):

        self.search_engine = WebSearch()

        self.fetch_engine = FetchPage()

        self.summary_engine = Summarizer()

        self.report_exporter = ReportExporter()

    # =====================================================
    # Public API
    # =====================================================

    def run(
        self,
        query: str,
        settings: dict
    ) -> dict:

        start_time = time.time()

        max_results = settings.get(
            "max_results",
            10
        )

        # -------------------------------------------------
        # Step 1
        # Search
        # -------------------------------------------------

        search_results = self.search_engine.search(
            query=query,
            max_results=max_results
        )

        # -------------------------------------------------
        # Step 2
        # Fetch Content
        # -------------------------------------------------

        pages = self.fetch_engine.fetch(
            search_results=search_results,
            max_pages=max_results
        )

        # -------------------------------------------------
        # Step 3
        # Summarize
        # -------------------------------------------------

        pages = self.summary_engine.generate(
            pages
        )

        # -------------------------------------------------
        # Step 4
        # Export Report
        # -------------------------------------------------

        report = self.report_exporter.export(
            query=query,
            pages=pages
        )

        # -------------------------------------------------
        # Statistics
        # -------------------------------------------------

        elapsed = round(
            time.time() - start_time,
            2
        )

        return {

            "success": True,

            "status": "Completed",

            "message": "Research completed successfully.",

            "statistics": {

                "retrieved": len(search_results),

                "filtered": len(search_results),

                "downloaded": len(pages),

                "time": elapsed

            },

            "report": report

        }