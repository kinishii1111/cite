import argparse
import sys

from cite.graph import build_graph
from cite.ingest import ingest


def main() -> None:
    parser = argparse.ArgumentParser(prog="cite", description="Agentic/Corrective RAG CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("ingest", help="Ingerir docs/ no Chroma")
    sub.add_parser("eval", help="Avaliar pipeline (TODO)")

    ask = sub.add_parser("ask", help="Perguntar ao grafo")
    ask.add_argument("question", help="Pergunta")
    ask.add_argument("--thread", default="default", help="thread_id")

    args = parser.parse_args()

    if args.command == "ingest":
        sys.exit(ingest())

    if args.command == "eval":
        print("TODO: eval ainda não implementado")
        return

    graph = build_graph()
    result = graph.invoke(
        {"question": args.question, "messages": []},
        config={"configurable": {"thread_id": args.thread}},
    )
    print(result)


if __name__ == "__main__":
    main()
