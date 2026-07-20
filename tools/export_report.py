import os


def export_report(topic, summaries):
    """
    Export the research result as a Markdown report.
    """

    output_folder = "research/final"
    os.makedirs(output_folder, exist_ok=True)

    report_path = os.path.join(output_folder, "report.md")

    with open(report_path, "w", encoding="utf-8") as file:

        file.write("# Research Report\n\n")

        file.write("## Topic\n\n")
        file.write(f"{topic}\n\n")

        file.write("---\n\n")

        for index, item in enumerate(summaries, start=1):

            file.write(f"## Source {index}\n\n")

            file.write("### Title\n\n")
            file.write(f"{item['title']}\n\n")

            file.write("### Summary\n\n")
            file.write(f"{item['summary']}\n\n")

            file.write("### URL\n\n")
            file.write(f"{item['url']}\n\n")

            file.write("---\n\n")

    print("\nMarkdown report generated.")
    print(report_path)