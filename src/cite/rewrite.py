from cite.state import CiteState


def rewrite(state: CiteState) -> dict:
    question = state.get("question", "")
    count = state.get("rewrite_count", 0) + 1
    result = {
        "question": question,
        "rewrite_count": count,
    }
    if count >= 3:
        result["documents"] = ["(placeholder)"]
    return result
