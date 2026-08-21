"""Memória por thread_id via SqliteSaver (LangGraph checkpoint)."""

from __future__ import annotations

import sqlite3
from pathlib import Path

from langgraph.checkpoint.sqlite import SqliteSaver

DEFAULT_DB = Path(__file__).resolve().parent.parent.parent / "data" / "checkpoints.sqlite"


def get_checkpointer(db_path: str | Path | None = None) -> SqliteSaver:
    """Retorna SqliteSaver pronto para `compile(checkpointer=...)`."""
    path = Path(db_path) if db_path else DEFAULT_DB
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(path), check_same_thread=False)
    return SqliteSaver(conn)