"""Ground — checa se a generation está ancorada nos documents."""
from __future__ import annotations

from cite.llm import get_llm
from cite.state import CiteState

REFUSE = (
    "Não encontrei essa informação na base KinSolo, então não posso "
    "responder sem inventar. Consulte uma fonte oficial."
)


def ground(state: CiteState) -> dict:
    generation = state.get("generation", "")
    docs = state.get("documents", [])
    if not docs or not generation:
        return {}

    # Sem docs úteis ou já reescrevemos bastante → recusa (não inventar).
    if state.get("rewrite_count", 0) >= 2:
        return {"generation": REFUSE}

    try:
        llm = get_llm()
        prompt = (
            "A resposta abaixo está ancorada (apoiada) nos documentos fornecidos? "
            "Responda APENAS 'sim' ou 'nao'.\n"
            f"Resposta: {generation}\n\nDocumentos:\n"
            + "\n".join(f"- {d}" for d in docs)
        )
        verdict = llm.invoke(prompt).content.strip().lower()
        if verdict.startswith("nao"):
            return {"generation": REFUSE}
    except RuntimeError:
        pass

    return {}
