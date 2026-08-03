"""
Enterprise Search Ranking Engine

M3.2

Calculates the final ranking score
for search results.
"""


class Ranking:

    def __init__(self):

        self.automotive_keywords = {

            "automotive",

            "vehicle",

            "car",

            "adas",

            "autonomous",

            "autonomous driving",

            "software defined vehicle",

            "sdv",

            "ecu",

            "autosar",

            "iso26262"

        }

        self.ai_keywords = {

            "ai",

            "artificial intelligence",

            "machine learning",

            "deep learning",

            "llm",

            "rag",

            "agent",

            "azure",

            "openai",

            "copilot"

        }

    # =====================================================
    # Public API
    # =====================================================

    def score(
        self,
        result: dict
    ) -> int:

        score = result.get(
            "quality_score",
            0
        )

        title = result.get(
            "title",
            ""
        ).lower()

        snippet = result.get(
            "snippet",
            ""
        ).lower()

        # --------------------------------------------
        # Automotive Keywords
        # --------------------------------------------

        for keyword in self.automotive_keywords:

            if keyword in title:

                score += 3

            elif keyword in snippet:

                score += 1

        # --------------------------------------------
        # AI Keywords
        # --------------------------------------------

        for keyword in self.ai_keywords:

            if keyword in title:

                score += 2

            elif keyword in snippet:

                score += 1

        return score

    # =====================================================
    # Sort Results
    # =====================================================

    def sort(
        self,
        results: list
    ) -> list:

        for item in results:

            item["final_score"] = self.score(
                item
            )

        results.sort(

            key=lambda x: x["final_score"],

            reverse=True

        )

        return results