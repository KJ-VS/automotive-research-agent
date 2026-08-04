"""
Enterprise Analytics Engine

Version
-------
V1.3.4

Generates analytics for dashboard and report.

Future
------
V2.0
    LLM Analytics

V3.0
    RAG Analytics
"""


from urllib.parse import urlparse


class AnalyticsEngine:

    def __init__(self):

        pass

    # =====================================================
    # Public API
    # =====================================================

    def generate(
        self,
        pages: list
    ) -> dict:

        if not pages:

            return {

                "page_count": 0,

                "average_score": 0,

                "average_domain_score": 0,

                "average_content_length": 0,

                "best_domain": "-",

                "top_score": 0

            }

        total_score = 0
        total_domain = 0
        total_length = 0

        best_domain = "-"
        top_score = -1

        for page in pages:

            overall = page.get(
                "overall_score",
                0
            )

            domain = page.get(
                "domain_score",
                0
            )

            content = page.get(
                "content",
                ""
            )

            total_score += overall
            total_domain += domain
            total_length += len(content)

            if overall > top_score:

                top_score = overall

                best_domain = self._extract_domain(

                    page.get(
                        "url",
                        ""
                    )

                )

        return {

            "page_count": len(pages),

            "average_score": round(

                total_score / len(pages),

                1

            ),

            "average_domain_score": round(

                total_domain / len(pages),

                1

            ),

            "average_content_length": int(

                total_length / len(pages)

            ),

            "best_domain": best_domain,

            "top_score": top_score

        }

    # =====================================================
    # Helper
    # =====================================================

    def _extract_domain(
        self,
        url: str
    ) -> str:

        try:

            return urlparse(

                url

            ).netloc.replace(

                "www.",

                ""

            )

        except Exception:

            return "-"