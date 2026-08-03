"""
Enterprise Web Search

Acts as the orchestrator of the search pipeline.

Responsibilities
----------------
1. Build search query
2. Execute DDGS search
3. Parse raw search results
4. Filter low-quality domains
5. Rank search results

Version
-------
M3.2 Final
"""

from ddgs import DDGS

from tools.query_builder import QueryBuilder
from tools.result_parser import ResultParser
from tools.domain_filter import DomainFilter
from tools.ranking import Ranking


class WebSearch:
    """
    Enterprise Search Orchestrator.
    """

    def __init__(self):

        self.engine = DDGS()

        self.query_builder = QueryBuilder()

        self.result_parser = ResultParser()

        self.domain_filter = DomainFilter()

        self.ranking = Ranking()

    # ======================================================
    # Public API
    # ======================================================

    def search(
        self,
        query: str,
        max_results: int = 10
    ) -> list:

        if not query.strip():

            return []

        # --------------------------------------------------
        # Step 1
        # Build Query
        # --------------------------------------------------

        search_query = self.query_builder.build(query)

        try:

            raw_results = list(

                self.engine.text(

                    search_query,

                    max_results=max_results

                )

            )

        except Exception as e:

            print(f"Search error: {e}")

            return []

        # --------------------------------------------------
        # Step 2
        # Parse Results
        # --------------------------------------------------

        results = self.result_parser.parse(

            raw_results

        )

        # --------------------------------------------------
        # Step 3
        # Domain Filter
        # --------------------------------------------------

        filtered = []

        visited = set()

        for item in results:

            url = item["url"]

            if url in visited:

                continue

            visited.add(url)

            if not self.domain_filter.is_allowed(url):

                continue

            item["quality_score"] = (

                self.domain_filter.quality_score(

                    url

                )

            )

            filtered.append(item)

        # --------------------------------------------------
        # Step 4
        # Ranking
        # --------------------------------------------------

        ranked = self.ranking.sort(

            filtered

        )

        return ranked