"""
Enterprise Query Builder

Version
-------
V1.3.1

Builds optimized search queries by
expanding domain-specific keywords.
"""

from typing import Dict, List


MAX_EXPANSION_TERMS = 15


class QueryBuilder:
    """
    Enterprise Query Builder.
    """

    def __init__(self):

        self.keyword_map: Dict[str, List[str]] = {

            # =====================================================
            # Automotive
            # =====================================================

            "adas": [

                "advanced driver assistance systems",

                "autonomous driving",

                "automotive"

            ],

            "sdv": [

                "software defined vehicle",

                "vehicle software platform",

                "automotive"

            ],

            "ecu": [

                "electronic control unit",

                "automotive"

            ],

            "autosar": [

                "adaptive autosar",

                "classic autosar"

            ],

            "iso26262": [

                "functional safety"

            ],

            # =====================================================
            # AI
            # =====================================================

            "ai": [

                "artificial intelligence",

                "generative ai"

            ],

            "genai": [

                "generative ai",

                "large language model"

            ],

            "llm": [

                "large language model",

                "foundation model"

            ],

            "rag": [

                "retrieval augmented generation",

                "vector database"

            ],

            "agent": [

                "ai agent",

                "multi agent"

            ],

            # =====================================================
            # Cloud
            # =====================================================

            "azure": [

                "microsoft azure",

                "azure openai",

                "azure ai"

            ],

            "kubernetes": [

                "k8s",

                "aks"

            ],

            "docker": [

                "container",

                "docker container"

            ]
        }

    # =====================================================
    # Public API
    # =====================================================

    def build(
        self,
        query: str
    ) -> str:

        if not query:

            return ""

        query = query.strip()

        tokens = self._tokenize(query)

        expansions = self._expand(tokens)

        return self._merge(query, expansions)

    # =====================================================
    # Tokenize
    # =====================================================

    def _tokenize(
        self,
        query: str
    ) -> List[str]:

        return [

            token.lower()

            for token in query.split()

        ]

    # =====================================================
    # Expand
    # =====================================================

    def _expand(
        self,
        tokens: List[str]
    ) -> List[str]:

        expanded = []

        for token in tokens:

            if token in self.keyword_map:

                expanded.extend(

                    self.keyword_map[token]

                )

        return expanded

    # =====================================================
    # Merge
    # =====================================================

    def _merge(
        self,
        original: str,
        expanded: List[str]
    ) -> str:

        result = [original]

        visited = {

            original.lower()

        }

        count = 0

        for keyword in expanded:

            key = keyword.lower()

            if key in visited:

                continue

            visited.add(key)

            result.append(keyword)

            count += 1

            if count >= MAX_EXPANSION_TERMS:

                break

        return " ".join(result)