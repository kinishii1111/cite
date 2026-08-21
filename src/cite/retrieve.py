from cite.state import CiteState


def retrieve(state: CiteState) -> dict:
    if state.get("documents"):
        return {}
    return {"documents": []}
