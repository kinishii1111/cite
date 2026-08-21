"""Helper de LLM Cite — ChatGroq temp=0."""
from __future__ import annotations

import os

from dotenv import load_dotenv

MODEL = "openai/gpt-oss-20b"


def get_llm():
    load_dotenv()
    key = os.getenv("GROQ_API_KEY")
    if not key:
        raise RuntimeError(
            "GROQ_API_KEY ausente. Defina GROQ_API_KEY no ambiente ou em .env "
            "(veja .env.example) e rode de novo."
        )
    from langchain_groq import ChatGroq

    return ChatGroq(model=MODEL, api_key=key, temperature=0)
