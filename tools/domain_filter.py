"""
Enterprise Domain Filter

Evaluates search result domains and
filters low-quality websites.

Version
-------
M3.2 Final
"""

from pathlib import Path
from urllib.parse import urlparse
from typing import Dict, List

import yaml


class DomainFilter:
    """
    Domain quality evaluation.

    Responsibilities
    ----------------
    - Normalize domains
    - Block unwanted domains
    - Evaluate domain quality
    """

    def __init__(self):

        self.config = self._load_config()

    # ======================================================
    # Configuration
    # ======================================================

    def _load_config(self) -> Dict:

        config_path = Path("config/domains.yaml")

        default = {

            "high_quality_domains": [],

            "medium_quality_domains": [],

            "blocked_domains": []

        }

        if not config_path.exists():

            return default

        try:

            with open(

                config_path,

                "r",

                encoding="utf-8"

            ) as file:

                data = yaml.safe_load(file)

                if data is None:

                    return default

                return data

        except Exception as e:

            print(f"Failed to load domains.yaml: {e}")

            return default

    # ======================================================
    # Public API
    # ======================================================

    def is_allowed(
        self,
        url: str
    ) -> bool:

        domain = self._normalize_domain(url)

        return not self._is_blocked(domain)

    def quality_score(
        self,
        url: str
    ) -> int:

        domain = self._normalize_domain(url)

        level = self._domain_level(domain)

        if level == "HIGH":

            return 10

        if level == "MEDIUM":

            return 5

        if level == "LOW":

            return 2

        return 3

    # ======================================================
    # Internal Helpers
    # ======================================================

    def _normalize_domain(
        self,
        url: str
    ) -> str:

        try:

            domain = urlparse(url).netloc.lower()

            prefixes = (

                "www.",

                "m.",

                "blog."

            )

            for prefix in prefixes:

                if domain.startswith(prefix):

                    domain = domain[len(prefix):]

            return domain

        except Exception:

            return ""

    def _is_blocked(
        self,
        domain: str
    ) -> bool:

        blocked: List[str] = self.config.get(

            "blocked_domains",

            []

        )

        return any(

            item in domain

            for item in blocked

        )

    def _domain_level(
        self,
        domain: str
    ) -> str:

        high = self.config.get(

            "high_quality_domains",

            []

        )

        if any(item in domain for item in high):

            return "HIGH"

        medium = self.config.get(

            "medium_quality_domains",

            []

        )

        if any(item in domain for item in medium):

            return "MEDIUM"

        # Well-known reference websites

        if "ieee.org" in domain:

            return "HIGH"

        if "arxiv.org" in domain:

            return "HIGH"

        if "github.com" in domain:

            return "HIGH"

        if "wikipedia.org" in domain:

            return "LOW"

        if "linkedin.com" in domain:

            return "LOW"

        return "NORMAL"