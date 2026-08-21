"""Embeddings Cite — default leve (Chroma ONNX); HF/MiniLM via CITE_EMBED=hf (VM)."""
from __future__ import annotations

import os
from typing import Any


def embed_mode() -> str:
    return os.environ.get("CITE_EMBED", "default").strip().lower()


def make_embedding_function() -> Any:
    """Retorna embedding function compatível com chromadb Collection."""
    mode = embed_mode()
    if mode in ("hf", "minilm", "sentence", "sentence-transformers"):
        # Pesado (torch) — use na VM: CITE_EMBED=hf
        from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

        return SentenceTransformerEmbeddingFunction(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
    from chromadb.utils.embedding_functions import DefaultEmbeddingFunction

    return DefaultEmbeddingFunction()
