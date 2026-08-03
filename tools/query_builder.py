"""
Enterprise Query Builder

Builds optimized search queries for
the Automotive Research Agent.

Version
-------
M3.2 Final
"""


from typing import Dict, List


class QueryBuilder:
    """
    Query enhancement module.

    Converts a short user query into a richer
    search query while keeping it concise.
    """

    def __init__(self):

        self.keyword_map: Dict[str, List[str]] = {

            "adas": [
                "automotive",
                "autonomous driving"
            ],

            "automotive": [
                "vehicle",
                "software defined vehicle"
            ],

            "sdv": [
                "software defined vehicle"
            ],

            "ai": [
                "artificial intelligence"
            ],

            "llm": [
                "large language model"
            ],

            "rag": [
                "retrieval augmented generation"
            ],

            "agent": [
                "multi agent"
            ],

            "azure": [
                "microsoft",
                "azure openai"
            ],

            "python": [
                "programming"
            ],

            "kubernetes": [
                "k8s",
                "aks"
            ]
        }

    # ==========================================================
    # Public API
    # ==========================================================

    def build(
        self,
        query: str
    ) -> str:
        """
        Build an enhanced search query.
        """

        if not query:

            return ""

        query = query.strip()

        tokens = self._tokenize(query)

        expanded = self._expand(tokens)

        merged = self._merge(query, expanded)

        return merged

    # ==========================================================
    # Tokenize
    # ==========================================================

    def _tokenize(
        self,
        query: str
    ) -> List[str]:

        return [

            token.lower()

            for token in query.split()

        ]

    # ==========================================================
    # Expand Keywords
    # ==========================================================

    def _expand(
        self,
        tokens: List[str]
    ) -> List[str]:

        keywords = []

        for token in tokens:

            if token in self.keyword_map:

                keywords.extend(

                    self.keyword_map[token]

                )

        return keywords

    # ==========================================================
    # Merge Query
    # ==========================================================

    def _merge(
        self,
        original: str,
        keywords: List[str]
    ) -> str:

        result = [original]

        visited = {

            original.lower()

        }

        for keyword in keywords:

            key = keyword.lower()

            if key in visited:

                continue

            visited.add(key)

            result.append(keyword)

        return " ".join(result)