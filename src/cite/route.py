from cite.state import CiteState

GENERAL_CONCEPTS = ("langgraph", "rag", "o que é")


def route(state: CiteState) -> dict:
    """Stub: pergunta factuais → retrieve; conceitos gerais → skip."""
    question = state.get("question", "").strip().lower()
    if "?" in question and not any(c in question for c in GENERAL_CONCEPTS):
        return {"question": state.get("question", "")}
    return {
        "question": state.get("question", ""),
        "documents": [],
        "skip_retrieve": True,
    }
