"""
Enterprise Domain Authority Engine

Version
-------
V1.3.2

Evaluates website authority and determines
whether a search result should participate
in ranking.
"""

import os
import yaml
from urllib.parse import urlparse


class DomainFilter:

    def __init__(self):

        self.config = self._load_config()

    # ==========================================================
    # Load Configuration
    # ==========================================================

    def _load_config(self):

        config_path = os.path.join(
            "config",
            "domains.yaml"
        )

        default = {

            "high_quality_domains": [],

            "medium_quality_domains": [],

            "blocked_domains": []

        }

        if not os.path.exists(config_path):

            return default

        try:

            with open(
                config_path,
                "r",
                encoding="utf-8"
            ) as f:

                data = yaml.safe_load(f)

                if data is None:

                    return default

                return data

        except Exception as e:

            print(f"Domain config error: {e}")

            return default

    # ==========================================================
    # Public API
    # ==========================================================

    def is_allowed(self, url: str) -> bool:

        domain = self._extract_domain(url)

        for blocked in self.config.get(
            "blocked_domains",
            []
        ):

            if blocked in domain:

                return False

        return True

    # ==========================================================
    # Domain Authority
    # ==========================================================

    def quality_score(self, url: str) -> int:

        domain = self._extract_domain(url)

        # -----------------------------
        # Blocked
        # -----------------------------

        for item in self.config.get(
            "blocked_domains",
            []
        ):

            if item in domain:

                return 0

        # -----------------------------
        # Enterprise / OEM
        # -----------------------------

        enterprise = [

            "bosch.com",

            "continental.com",

            "bmw.com",

            "mercedes-benz.com",

            "volkswagen.com",

            "vw.com",

            "aptiv.com",

            "valeo.com",

            "nvidia.com",

            "microsoft.com",

            "azure.microsoft.com",

            "openai.com"

        ]

        for item in enterprise:

            if item in domain:

                return 10

        # -----------------------------
        # Research
        # -----------------------------

        research = [

            "ieee.org",

            "arxiv.org",

            "springer.com",

            "nature.com",

            "sciencedirect.com",

            "fraunhofer.de"

        ]

        for item in research:

            if item in domain:

                return 9

        # -----------------------------
        # Open Source
        # -----------------------------

        opensource = [

            "github.com",

            "huggingface.co"

        ]

        for item in opensource:

            if item in domain:

                return 8

        # -----------------------------
        # Medium Quality
        # -----------------------------

        for item in self.config.get(
            "medium_quality_domains",
            []
        ):

            if item in domain:

                return 6

        # -----------------------------
        # Wikipedia
        # -----------------------------

        if "wikipedia.org" in domain:

            return 5

        # -----------------------------
        # Government
        # -----------------------------

        if domain.endswith(".gov"):

            return 8

        if domain.endswith(".gov.uk"):

            return 8

        if domain.endswith(".eu"):

            return 7

        # -----------------------------
        # Universities
        # -----------------------------

        if domain.endswith(".edu"):

            return 8

        if domain.endswith(".ac.uk"):

            return 8

        # -----------------------------
        # LinkedIn
        # -----------------------------

        if "linkedin.com" in domain:

            return 2

        # -----------------------------
        # Social Media
        # -----------------------------

        social = [

            "facebook.com",

            "instagram.com",

            "x.com",

            "twitter.com",

            "tiktok.com"

        ]

        for item in social:

            if item in domain:

                return 1

        # -----------------------------
        # Unknown
        # -----------------------------

        return 4

    # ==========================================================
    # Category
    # ==========================================================

    def category(self, url: str) -> str:

        domain = self._extract_domain(url)

        if any(x in domain for x in [

            "bosch",

            "bmw",

            "continental",

            "volkswagen",

            "mercedes",

            "aptiv",

            "valeo"

        ]):

            return "OEM / Automotive"

        if any(x in domain for x in [

            "ieee",

            "arxiv",

            "springer",

            "nature",

            "fraunhofer"

        ]):

            return "Research"

        if any(x in domain for x in [

            "github",

            "huggingface"

        ]):

            return "Open Source"

        if "wikipedia.org" in domain:

            return "Reference"

        if "linkedin.com" in domain:

            return "Social"

        return "General"

    # ==========================================================
    # Normalize Domain
    # ==========================================================

    def _extract_domain(self, url: str) -> str:

        try:

            domain = urlparse(url).netloc.lower()

            domain = domain.replace(
                "www.",
                ""
            )

            return domain

        except Exception:

            return ""