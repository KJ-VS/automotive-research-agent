from tools.web_search import web_search
from tools.fetch_page import fetch_page
from tools.summarize import summarize
from tools.export_report import export_report


class ResearchAgent:

    def run(self, topic):

        print(f"\nResearch Topic: {topic}")

        # Search
        urls = web_search(topic)

        print("\nSearch Results:\n")
        print(urls)

        # Fetch
        pages = fetch_page(urls)

        print(f"\nDownloaded Pages: {len(pages)}")

        # Summarize
        summaries = summarize(pages)

        print(f"Generated Summaries: {len(summaries)}")

        # Export
        export_report(topic, summaries)

        print("\nResearch completed.")