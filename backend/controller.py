"""
Controller Layer

Acts as the bridge between the UI and the backend workflow.

Responsibilities
----------------
- Validate user input
- Start research workflow
- Handle workflow errors
- Return a standardized result object

Future
------
V2
    Azure OpenAI

V3
    RAG Retrieval

V4
    Multi-Agent Workflow
"""

from backend.workflow import Workflow


class Controller:

    def __init__(self):

        self.workflow = Workflow()

    # ==========================================================
    # Public API
    # ==========================================================

    def start_research(
        self,
        query: str,
        settings: dict
    ) -> dict:

        # ------------------------------------------
        # Validate Input
        # ------------------------------------------

        validation = self._validate_query(query)

        if validation is not None:
            return validation

        # ------------------------------------------
        # Execute Workflow
        # ------------------------------------------

        try:

            result = self.workflow.run(
                query=query,
                settings=settings
            )

            return result

        except Exception as e:

            return self._error_result(str(e))

    # ==========================================================
    # Validation
    # ==========================================================

    def _validate_query(
        self,
        query: str
    ):

        if query is None:

            return self._error_result(
                "Research topic is missing."
            )

        if not query.strip():

            return self._error_result(
                "Please enter a research topic."
            )

        return None

    # ==========================================================
    # Error Handling
    # ==========================================================

    def _error_result(
        self,
        message: str
    ) -> dict:

        return {

            "success": False,

            "status": "Error",

            "message": message,

            "statistics": {

                "retrieved": 0,

                "filtered": 0,

                "downloaded": 0,

                "time": 0

            },

            "report": ""

        }