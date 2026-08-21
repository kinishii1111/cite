from cite.state import CiteState


def route(state: CiteState) -> dict:
    question = state.get("question", "")
    return {"question": question}
