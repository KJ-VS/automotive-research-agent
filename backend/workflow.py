"""
Workflow Layer

Coordinates the complete research pipeline.

Version
-------
V1.3

Pipeline
--------
Search
    ↓
Content Extraction
    ↓
Summarization
    ↓
Analytics
    ↓
Report Export
"""

import time

from tools.web_search import WebSearch
from tools.fetch_page import FetchPage
from tools.summarize import Summarizer
from tools.export_report import ReportExporter
from tools.analytics import AnalyticsEngine


class Workflow:
    """
    Enterprise Workflow Coordinator.
    """

    def __init__(self):

        self.search_engine = WebSearch()

        self.fetch_engine = FetchPage()

        self.summary_engine = Summarizer()

        self.analytics_engine = AnalyticsEngine()

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

        # =====================================================
        # Step 1
        # Search
        # =====================================================

        search_results = self.search_engine.search(

            query=query,

            max_results=max_results

        )

        # =====================================================
        # Step 2
        # Content Extraction
        # =====================================================

        pages = self.fetch_engine.fetch(

            search_results=search_results,

            max_pages=max_results

        )

        # =====================================================
        # Step 3
        # Summarization
        # =====================================================

        pages = self.summary_engine.generate(

            pages

        )

        # =====================================================
        # Step 4
        # Analytics
        # =====================================================

        analytics = self.analytics_engine.generate(

            pages

        )

        # =====================================================
        # Step 5
        # Report Export
        # =====================================================

        report = self.report_exporter.export(

            query=query,

            pages=pages

        )

        # =====================================================
        # Statistics
        # =====================================================

        elapsed = round(

            time.time() - start_time,

            2

        )

        statistics = {

            "retrieved": len(search_results),

            "filtered": len(search_results),

            "downloaded": len(pages),

            "time": elapsed

        }

        # =====================================================
        # Result
        # =====================================================

        return {

            "success": True,

            "status": "Completed",

            "message": "Research completed successfully.",

            "statistics": statistics,

            "analytics": analytics,

            "pages": pages,

            "report": report

        }