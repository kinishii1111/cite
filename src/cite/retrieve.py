"""Retrieve top-k no Chroma → state['documents']."""
from __future__ import annotations

from pathlib import Path

import chromadb

from cite.embeddings import make_embedding_function
from cite.state import CiteState

CHROMA_DIR = Path(__file__).resolve().parents[2] / "data" / "chroma"
COLLECTION = "cite_docs"
TOP_K = 3


def retrieve(state: CiteState) -> dict:
    if state.get("documents") or state.get("skip_retrieve"):
        return {}
    question = state.get("question", "")
    if not question.strip():
        return {"documents": []}
    if not CHROMA_DIR.exists():
        return {"documents": []}

    ef = make_embedding_function()
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    col = client.get_or_create_collection(name=COLLECTION, embedding_function=ef)
    results = col.query(query_texts=[question], n_results=TOP_K)

    docs_out: list[str] = []
    documents = (results.get("documents") or [[]])[0]
    metadatas = (results.get("metadatas") or [[]])[0]
    for page_content, meta in zip(documents, metadatas):
        meta = meta or {}
        source = meta.get("source", "?")
        section = meta.get("section", "")
        label = f"{source} / {section}" if section else source
        docs_out.append(f"[{label}]\n{page_content}")

    return {"documents": docs_out}
