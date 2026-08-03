"""
Enterprise Search Result Parser

Converts raw search engine results
into a unified internal format.

Version
-------
M3.2
"""


class ResultParser:

    def __init__(self):

        pass

    # ==========================================================
    # Public API
    # ==========================================================

    def parse(
        self,
        raw_results
    ) -> list:

        results = []

        if raw_results is None:

            return results

        for item in raw_results:

            parsed = self._parse_item(item)

            if parsed is not None:

                results.append(parsed)

        return results

    # ==========================================================
    # Parse One Result
    # ==========================================================

    def _parse_item(
        self,
        item
    ):

        if item is None:

            return None

        if not isinstance(item, dict):

            return None

        # ----------------------------------------
        # URL
        # ----------------------------------------

        url = item.get("href")

        if not url:

            url = item.get("url", "")

        if not url:

            return None

        # ----------------------------------------
        # Title
        # ----------------------------------------

        title = item.get(
            "title",
            ""
        ).strip()

        if title == "":

            return None

        # ----------------------------------------
        # Snippet
        # ----------------------------------------

        snippet = item.get(
            "body",
            ""
        ).strip()

        # ----------------------------------------
        # Source
        # ----------------------------------------

        source = item.get(
            "source",
            ""
        )

        # ----------------------------------------
        # Unified Result
        # ----------------------------------------

        return {

            "title": title,

            "url": url,

            "snippet": snippet,

            "source": source,

            "quality_score": 0,

            "final_score": 0

        }