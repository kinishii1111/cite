"""Generate — resposta em PT com citação; recusa se não houver docs."""
from __future__ import annotations

from cite.llm import get_llm
from cite.state import CiteState

REFUSE = (
    "Não encontrei essa informação na base KinSolo, então não posso "
    "responder sem inventar. Consulte uma fonte oficial."
)


def generate(state: CiteState) -> dict:
    docs = state.get("documents", [])
    question = state.get("question", "")

    if not docs:
        return {"generation": REFUSE}

    try:
        llm = get_llm()
        prompt = (
            "Responda em português, com base APENAS nos documentos abaixo. "
            "Inclua citação da fonte entre colchetes no final da frase "
            "(ex.: [fonte.md]). Se a informação não estiver nos documentos, "
            "responda: 'Não encontrei essa informação na base KinSolo.'\n"
            f"Pergunta: {question}\n\nDocumentos:\n"
        )
        for doc in docs:
            prompt += f"- {doc}\n"
        generation = llm.invoke(prompt).content.strip()
    except RuntimeError:
        generation = REFUSE

    return {"generation": generation}
