"""Route — roteia: conceito geral → skip; pergunta factual com ? → retrieve."""
from cite.state import CiteState

GENERAL_CONCEPTS = ("langgraph", "rag", "o que é")


def route(state: CiteState) -> dict:
    question = state.get("question", "").strip()
    q = question.lower()
    if "?" in q and not any(c in q for c in GENERAL_CONCEPTS):
        return {"question": question}
    return {
        "question": question,
        "documents": [],
        "skip_retrieve": True,
    }
