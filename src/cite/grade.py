"""Grade — filtra documentos irrelevantes à pergunta."""
from __future__ import annotations

from cite.llm import get_llm
from cite.state import CiteState


def grade_docs(state: CiteState) -> dict:
    docs = state.get("documents", [])
    question = state.get("question", "")
    if not docs or not question.strip():
        return {}

    try:
        llm = get_llm()
        prompt = (
            "Você é um revisor de recuperação (RAG). Para cada documento abaixo, "
            "responda APENAS com 'sim' ou 'nao' por linha, na mesma ordem, "
            "indicando se o documento é relevante para responder à pergunta.\n"
            f"Pergunta: {question}\n\nDocumentos:\n"
        )
        for i, doc in enumerate(docs):
            prompt += f"{i}: {doc}\n"
        result = llm.invoke(prompt).content.strip().splitlines()

        kept = [
            doc for i, doc in enumerate(docs)
            if i < len(result) and result[i].strip().lower().startswith("sim")
        ]
    except RuntimeError:
        # Sem GROQ_API_KEY: fallback heurístico — mantém tudo (retrieve já filtrou).
        kept = docs

    return {"documents": kept}
