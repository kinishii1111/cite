from cite.state import CiteState


def ground(state: CiteState) -> dict:
    generation = state.get("generation", "")
    return {"generation": generation}
