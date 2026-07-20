from ddgs import DDGS


BLOCKED_DOMAINS = {
    "wikipedia.org",
    "linkedin.com",
    "facebook.com",
    "instagram.com",
    "twitter.com",
    "x.com",
    "tiktok.com"
}


MAX_SEARCH_RESULTS = 15


def web_search(topic):
    """
    Search the web and return candidate URLs.

    Returns up to MAX_SEARCH_RESULTS filtered URLs.
    """

    urls = []

    with DDGS() as ddgs:

        results = ddgs.text(
            topic,
            max_results=30
        )

        for result in results:

            url = result.get("href")

            if not url:
                continue

            if any(domain in url for domain in BLOCKED_DOMAINS):

                print(f"Skip: {url}")
                continue

            print(f"Keep: {url}")

            urls.append(url)

            if len(urls) >= MAX_SEARCH_RESULTS:
                break

    return urls