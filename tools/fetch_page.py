"""
Enterprise Content Extraction

M3.3

Downloads web pages and extracts the
main article content.

Pipeline

Search Result
        │
        ▼
Download HTML
        │
        ▼
Trafilatura
        │
        ▼
BeautifulSoup (Fallback)
        │
        ▼
Content Cleaning
        │
        ▼
Cache
"""

import os
import requests
import trafilatura

from bs4 import BeautifulSoup


DEFAULT_MAX_PAGES = 5
DEFAULT_MAX_CONTENT_LENGTH = 8000


class FetchPage:
    """
    Enterprise Content Extraction Engine.
    """

    def __init__(self):

        self.headers = {

            "User-Agent": (

                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/138.0 Safari/537.36"

            )

        }

        self.cache_folder = os.path.join(

            "research",

            "cache"

        )

        os.makedirs(

            self.cache_folder,

            exist_ok=True

        )

    # =====================================================
    # Public API
    # =====================================================

    def fetch(
        self,
        search_results: list,
        max_pages: int = DEFAULT_MAX_PAGES,
        max_content_length: int = DEFAULT_MAX_CONTENT_LENGTH
    ) -> list:

        """
        Download and extract page contents.

        Parameters
        ----------
        search_results

            Search results returned by WebSearch.

        max_pages

            Maximum pages to download.

        max_content_length

            Maximum stored content length.

        Returns
        -------
        list
        """

        pages = []

        for result in search_results:

            if len(pages) >= max_pages:

                break

            url = result["url"]

            print(f"\nDownloading: {url}")

            try:

                response = requests.get(

                    url,

                    headers=self.headers,

                    timeout=10,

                    allow_redirects=True

                )

                response.raise_for_status()

                html = response.text

                title = self.extract_title(html)

                content = self.extract_with_trafilatura(html)

                if content:

                    print("Trafilatura extraction successful.")

                else:

                    print(
                        "Trafilatura failed. Using BeautifulSoup..."
                    )

                    content = self.extract_with_bs4(html)

                content = self.clean_text(content)

                if len(content) < 100:

                    print("Ignored (content too short).")

                    continue

                content = content[:max_content_length]

                page = {

                    "title": title,

                    "url": url,

                    "content": content,

                    "quality_score": result.get(

                        "quality_score",

                        0

                    ),

                    "final_score": result.get(

                        "final_score",

                        0

                    )

                }

                pages.append(page)

                self.save_cache(

                    len(pages),

                    title,

                    content

                )

            except Exception as e:

                print(f"Failed: {url}")

                print(e)

                continue

        print(

            f"\nCollected {len(pages)} pages."

        )

        return pages

        # =====================================================
    # Helper Functions
    # =====================================================

    def extract_title(
        self,
        html: str
    ) -> str:

        soup = BeautifulSoup(

            html,

            "html.parser"

        )

        if soup.title and soup.title.string:

            return soup.title.string.strip()

        return "Unknown Title"

    # =====================================================

    def extract_with_trafilatura(
        self,
        html: str
    ) -> str:

        return trafilatura.extract(

            html,

            include_comments=False,

            include_tables=True,

            include_images=False,

            favor_precision=True

        ) or ""

    # =====================================================

    def extract_with_bs4(
        self,
        html: str
    ) -> str:

        soup = BeautifulSoup(

            html,

            "html.parser"

        )

        # Remove noisy elements

        for tag in soup([

            "script",

            "style",

            "nav",

            "header",

            "footer",

            "aside",

            "noscript",

            "svg",

            "form",

            "iframe",

            "button",

            "input"

        ]):

            tag.decompose()

        content = (

            soup.find("article")

            or soup.find("main")

            or soup.find(id="content")

            or soup.find(class_="content")

            or soup.find(class_="article")

            or soup.find(class_="post")

            or soup.find(class_="entry-content")

            or soup.find("body")

        )

        if content:

            return content.get_text(

                separator="\n",

                strip=True

            )

        return ""

    # =====================================================

    def clean_text(
        self,
        text: str
    ) -> str:

        if not text:

            return ""

        ignore_words = {

            "Home",

            "Menu",

            "Search",

            "Login",

            "Register",

            "Sign In",

            "Sign in",

            "Cookie",

            "Cookies",

            "Privacy",

            "Privacy Policy",

            "Terms",

            "Contact",

            "Newsletter",

            "Subscribe",

            "Back to top",

            "Previous",

            "Next"

        }

        lines = []

        seen = set()

        for line in text.splitlines():

            line = line.strip()

            if len(line) < 3:

                continue

            if line in ignore_words:

                continue

            if line in seen:

                continue

            seen.add(line)

            lines.append(line)

        return "\n".join(lines)

    # =====================================================

    def save_cache(
        self,
        index: int,
        title: str,
        content: str
    ) -> None:

        filename = os.path.join(

            self.cache_folder,

            f"page_{index}.txt"

        )

        with open(

            filename,

            "w",

            encoding="utf-8"

        ) as file:

            file.write(title)

            file.write("\n\n")

            file.write(content)

        print(

            f"Saved cache: {filename}"

        )