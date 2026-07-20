import os

import requests
import trafilatura
from bs4 import BeautifulSoup


TARGET_PAGES = 5


def fetch_page(urls):

    cache_folder = "research/cache"
    os.makedirs(cache_folder, exist_ok=True)

    pages = []

    headers = {
        "User-Agent": (
            "Mozilla/5.0 "
            "(Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/138.0 Safari/537.36"
        )
    }

    for url in urls:

        if len(pages) >= TARGET_PAGES:

            print(f"\nCollected {TARGET_PAGES} valid pages.")
            break

        print(f"\nDownloading: {url}")

        try:

            response = requests.get(
                url,
                headers=headers,
                timeout=10
            )

            response.raise_for_status()

            html = response.text

            title = extract_title(html)

            content = extract_with_trafilatura(html)

            if content:

                print("Content extracted using Trafilatura.")

            else:

                print("Trafilatura failed. Using BeautifulSoup fallback...")

                content = extract_with_bs4(html)

            content = clean_text(content)

            if len(content) < 100:

                print("No useful content found. Trying next URL...")

                continue

            pages.append({
                "title": title,
                "url": url,
                "content": content
            })

            save_cache(
                cache_folder,
                len(pages),
                title,
                content
            )

        except Exception as e:

            print(f"Failed: {url}")
            print(e)

            continue

    return pages


# ==========================================================
# Helper Functions
# ==========================================================

def extract_title(html):

    soup = BeautifulSoup(html, "html.parser")

    if soup.title and soup.title.string:

        return soup.title.string.strip()

    return "Unknown Title"


def extract_with_trafilatura(html):

    return trafilatura.extract(
        html,
        include_comments=False,
        include_tables=True
    )


def extract_with_bs4(html):

    soup = BeautifulSoup(html, "html.parser")

    for tag in soup([
        "script",
        "style",
        "nav",
        "header",
        "footer",
        "aside",
        "noscript",
        "form",
        "svg"
    ]):
        tag.decompose()

    content = (
        soup.find("article")
        or soup.find("main")
        or soup.find(id="content")
        or soup.find(class_="content")
        or soup.find(class_="article")
        or soup.find(class_="post")
        or soup.find("body")
    )

    if content:

        return content.get_text(
            separator="\n",
            strip=True
        )

    return ""


def clean_text(text):

    if not text:

        return ""

    lines = []
    seen = set()

    ignore_words = {
        "Home",
        "Menu",
        "Search",
        "Login",
        "Sign in",
        "Register",
        "Cookie",
        "Cookies",
        "Privacy",
        "Contact",
        "Subscribe",
        "Back to top",
        "Previous",
        "Next"
    }

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


def save_cache(folder, index, title, content):

    filename = os.path.join(
        folder,
        f"page_{index}.txt"
    )

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(title)
        f.write("\n\n")
        f.write(content)

    print(f"Saved: {filename}")