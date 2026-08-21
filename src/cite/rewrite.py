"""Rewrite — reformula a pergunta para busca melhor."""
from __future__ import annotations

from cite.llm import get_llm
from cite.state import CiteState


def rewrite(state: CiteState) -> dict:
    question = state.get("question", "")
    count = state.get("rewrite_count", 0) + 1
    result: dict = {"question": question, "rewrite_count": count}

    if count >= 2 and not state.get("documents"):
        # Sem docs úteis e já reescrevemos: não loop infinito — recusa em generate.
        result["documents"] = []
        return result

    try:
        llm = get_llm()
        prompt = (
            "Reescreva a pergunta abaixo para uma busca RAG mais eficaz. "
            "Devolva apenas a pergunta reformulada, em português.\n"
            f"Pergunta original: {question}"
        )
        rewritten = llm.invoke(prompt).content.strip()
        if rewritten:
            result["question"] = rewritten
    except RuntimeError:
        pass

    return result
