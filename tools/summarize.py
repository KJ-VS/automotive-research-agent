"""
Enterprise Summarization Engine

M3.3

Generates extractive summaries for
downloaded web pages.

Future
------
V2.0
    Azure OpenAI

V3.0
    RAG

V4.0
    Multi-Agent
"""

import re


DEFAULT_MAX_SENTENCES = 5
DEFAULT_FALLBACK_LENGTH = 500


class Summarizer:
    """
    Enterprise Extractive Summarizer.
    """

    def __init__(self):

        pass

    # =====================================================
    # Public API
    # =====================================================

    def generate(
        self,
        pages: list
    ) -> list:
        """
        Generate summaries for all pages.

        Parameters
        ----------
        pages
            List of extracted pages.

        Returns
        -------
        list
            Pages with an additional 'summary' field.
        """

        summarized_pages = []

        for page in pages:

            summary = self.extract_summary(

                page.get(

                    "content",

                    ""

                )

            )

            summarized_page = page.copy()

            summarized_page["summary"] = summary

            summarized_pages.append(

                summarized_page

            )

        return summarized_pages

    # =====================================================
    # Extractive Summary
    # =====================================================

    def extract_summary(
        self,
        text: str,
        max_sentences: int = DEFAULT_MAX_SENTENCES
    ) -> str:

        if not text:

            return ""

        text = text.replace(

            "\n",

            " "

        )

        text = re.sub(

            r"\s+",

            " ",

            text

        )

        sentences = re.split(

            r"(?<=[.!?])\s+",

            text

        )

        summary = []

        for sentence in sentences:

            sentence = sentence.strip()

            if len(sentence) < 40:

                continue

            summary.append(

                sentence

            )

            if len(summary) >= max_sentences:

                break

        if not summary:

            return text[:DEFAULT_FALLBACK_LENGTH]

        return "\n\n".join(summary)