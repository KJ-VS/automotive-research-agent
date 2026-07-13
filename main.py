from agent import ResearchAgent


def main():
    print("=== Automotive Research Agent ===")

    topic = input("Enter research topic: ")

    agent = ResearchAgent()

    agent.run(topic)


if __name__ == "__main__":
    main()