"""Ingestão Chroma dos docs/*.md."""
from __future__ import annotations

from pathlib import Path

import chromadb

from cite.embeddings import embed_mode, make_embedding_function

CHROMA_DIR = Path(__file__).resolve().parents[2] / "data" / "chroma"
DOCS_DIR = Path(__file__).resolve().parents[2] / "docs"
COLLECTION = "cite_docs"


def _chunk_markdown(text: str, source: str) -> list[tuple[str, dict]]:
    chunks: list[tuple[str, dict]] = []
    current: list[str] = []
    header = ""
    for line in text.splitlines():
        if line.startswith("## "):
            if current:
                body = "\n".join(current).strip()
                if body:
                    chunks.append((body, {"source": source, "section": header}))
            header = line[3:].strip()
            current = [line]
        else:
            current.append(line)
    if current:
        body = "\n".join(current).strip()
        if body:
            chunks.append((body, {"source": source, "section": header}))
    return chunks


def ingest() -> int:
    if not DOCS_DIR.is_dir():
        print(f"docs/ não encontrado em {DOCS_DIR}")
        return 1

    CHROMA_DIR.mkdir(parents=True, exist_ok=True)
    ef = make_embedding_function()
    client = chromadb.PersistentClient(path=str(CHROMA_DIR))
    col = client.get_or_create_collection(name=COLLECTION, embedding_function=ef)

    try:
        existing = set(col.get(include=[]).get("ids") or [])
    except Exception:
        existing = set()

    ids: list[str] = []
    docs: list[str] = []
    metas: list[dict] = []
    for md in sorted(DOCS_DIR.glob("*.md")):
        if md.name.lower() == "readme.md":
            continue
        text = md.read_text(encoding="utf-8")
        source = str(md.relative_to(DOCS_DIR))
        for page_content, meta in _chunk_markdown(text, source):
            doc_id = f"{meta['source']}:{meta['section'] or 'root'}"
            if doc_id in existing:
                continue
            ids.append(doc_id)
            docs.append(page_content)
            metas.append(meta)
            existing.add(doc_id)

    if ids:
        col.add(ids=ids, documents=docs, metadatas=metas)

    print(
        f"ingest: {len(ids)} chunks novos → {COLLECTION} "
        f"(embed={embed_mode()} | {CHROMA_DIR})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(ingest())
