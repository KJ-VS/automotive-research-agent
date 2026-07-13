from tools.web_search import web_search
from tools.fetch_page import fetch_page
from tools.export_report import export_report


class ResearchAgent:

    def run(self, topic):

        print(f"Research Topic: {topic}")

        search_results = web_search(topic)

        pages = fetch_page(search_results)

        export_report(topic, pages)

        print("Research completed.")