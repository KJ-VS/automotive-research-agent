"""
Enterprise Ranking Engine

Version
-------
V1.3.3

Calculates an explainable ranking score
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

    # ======================================================
    # Public API
    # ======================================================

    def score(
        self,
        result: dict
    ) -> dict:

        title = result.get(
            "title",
            ""
        ).lower()

        snippet = result.get(
            "snippet",
            ""
        ).lower()

        domain_score = result.get(
            "quality_score",
            0
        )

        # =====================================
        # Title Score
        # =====================================

        title_score = 0

        for keyword in self.automotive_keywords:

            if keyword in title:

                title_score += 4

        for keyword in self.ai_keywords:

            if keyword in title:

                title_score += 3

        title_score = min(
            title_score,
            30
        )

        # =====================================
        # Snippet Score
        # =====================================

        snippet_score = 0

        for keyword in self.automotive_keywords:

            if keyword in snippet:

                snippet_score += 2

        for keyword in self.ai_keywords:

            if keyword in snippet:

                snippet_score += 1

        snippet_score = min(
            snippet_score,
            20
        )

        # =====================================
        # Content Quality
        # =====================================

        content_score = 0

        length = len(snippet)

        if length > 300:

            content_score = 15

        elif length > 200:

            content_score = 12

        elif length > 120:

            content_score = 8

        else:

            content_score = 4

        # =====================================
        # Penalty
        # =====================================

        penalty = 0

        if "linkedin.com" in result.get(
            "url",
            ""
        ):

            penalty += 8

        if "wikipedia.org" in result.get(
            "url",
            ""
        ):

            penalty += 2

        # =====================================
        # Overall Score
        # =====================================

        overall = (

            domain_score * 4

            +

            title_score

            +

            snippet_score

            +

            content_score

            -

            penalty

        )

        # Maximum score = 105

        overall = min(
            overall,
            100
        )

        result["domain_score"] = domain_score

        result["title_score"] = title_score

        result["snippet_score"] = snippet_score

        result["content_score"] = content_score

        result["penalty"] = penalty

        result["overall_score"] = overall

        return result

    # ======================================================
    # Sort Results
    # ======================================================

    def sort(
        self,
        results: list
    ) -> list:

        ranked = []

        for item in results:

            ranked.append(

                self.score(item)

            )

        ranked.sort(

            key=lambda x: x["overall_score"],

            reverse=True

        )

        # =====================================
        # Rank
        # =====================================

        for index, item in enumerate(

            ranked,

            start=1

        ):

            item["rank"] = index

        return ranked