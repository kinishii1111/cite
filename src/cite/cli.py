import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

from cite.graph import build_graph
from cite.ingest import ingest

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def _need_key() -> bool:
    load_dotenv()
    if not os.getenv("GROQ_API_KEY"):
        print(
            "cite: exige GROQ_API_KEY no ambiente ou em .env (veja .env.example). "
            "Defina GROQ_API_KEY e rode de novo.",
            file=sys.stderr,
        )
        return True
    return False


def main() -> None:
    parser = argparse.ArgumentParser(prog="cite", description="Agentic/Corrective RAG CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("ingest", help="Ingerir docs/ no Chroma")
    sub.add_parser("eval", help="Avaliar pipeline via eval/golden.json")

    ask = sub.add_parser("ask", help="Perguntar ao grafo")
    ask.add_argument("question", help="Pergunta")
    ask.add_argument("--thread", default="default", help="thread_id")

    args = parser.parse_args()

    if args.command == "ingest":
        sys.exit(ingest())

    if args.command == "eval":
        if _need_key():
            sys.exit(1)
        from eval.run import run_eval

        sys.exit(run_eval())

    if _need_key():
        sys.exit(1)

    graph = build_graph()
    result = graph.invoke(
        {"question": args.question, "messages": []},
        config={"configurable": {"thread_id": args.thread}},
    )
    generation = result.get("generation", "")
    print(generation)


if __name__ == "__main__":
    main()
