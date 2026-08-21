import argparse

from cite.graph import build_graph


def main() -> None:
    parser = argparse.ArgumentParser(prog="cite", description="Agentic/Corrective RAG CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("ingest", help="Ingerir documentos (TODO)")
    sub.add_parser("eval", help="Avaliar pipeline (TODO)")

    ask = sub.add_parser("ask", help="Perguntar ao grafo")
    ask.add_argument("question", help="Pergunta")
    ask.add_argument("--thread", default="default", help="thread_id")

    args = parser.parse_args()

    if args.command == "ingest":
        print("TODO: ingest ainda não implementado")
        return

    if args.command == "eval":
        print("TODO: eval ainda não implementado")
        return

    graph = build_graph()
    result = graph.invoke(
        {"question": args.question, "messages": []},
        config={"configurable": {"thread_id": args.thread}},
    )
    print(result)
