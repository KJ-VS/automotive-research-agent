import re


def summarize(pages):
    """
    Create a simple extractive summary for each page.

    Input:
        [
            {
                "title": "...",
                "url": "...",
                "content": "..."
            }
        ]

    Output:
        [
            {
                "title": "...",
                "url": "...",
                "summary": "..."
                "source": "web"
            }
        ]
    """

    summaries = []

    for page in pages:

        title = page["title"]
        url = page["url"]
        content = page["content"]

        summary = extract_summary(content)

        summaries.append({
            "title": title,
            "url": url,
            "summary": summary
        })

    return summaries


def extract_summary(text, max_sentences=5):
    """
    Extract the first few meaningful sentences.
    """

    # Replace line breaks with spaces
    text = text.replace("\n", " ")

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', text)

    summary = []

    for sentence in sentences:

        sentence = sentence.strip()

        if len(sentence) < 40:
            continue

        summary.append(sentence)

        if len(summary) >= max_sentences:
            break

    if not summary:

        # Fallback:
        # If no complete sentence is found,
        # return the first 500 characters.
        return text[:500]

    return "\n\n".join(summary)