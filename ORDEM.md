# ORDEM — tarefa/c2-ingest

## Agente
opencode

## Objetivo
Ingestão Chroma dos docs/ + retrieve real. Embeddings locais (HuggingFace MiniLM / sentence-transformers). Sem nós LLM ainda.

## Copiar de
- docs/ já na main
- langchain_chroma + HuggingFaceEmbeddings (ou DefaultEmbeddingFunction do chromadb se HF falhar)
- data/chroma/ gitignored

## Fazer
1. `src/cite/ingest.py` — lê docs/*.md, chunk simples, persiste em `data/chroma`
2. `python -m cite ingest` no cli.py chama ingest real
3. `src/cite/retrieve.py` — busca top-k no Chroma; preenche state["documents"] com textos + source path
4. Ajustar `route.py` stub: se question contém "?" e não é conceito geral óbvio → retrieve; se "o que é langgraph" → documents=[] e skip (pode setar flag) — mínimo ok
5. Commit `opencode:`
6. NÃO implementar grade/generate LLM nesta ORDEM

## Arquivos permitidos
- src/cite/ingest.py
- src/cite/retrieve.py
- src/cite/route.py
- src/cite/cli.py
- pyproject.toml
- ORDEM.md
- NÃO mexer docs/ (já ok)

## Ownership
- src/cite/ingest.py
- src/cite/retrieve.py
- src/cite/route.py
- src/cite/cli.py
- pyproject.toml

## Pronto quando
```bash
cd /home/kin/Documents/estudo/langgraph-portfolio/trabalho/cite
pip install -e . -q
python -m cite ingest
PYTHONPATH=src python3 -c "
from cite.retrieve import retrieve
s=retrieve({'question':'prazo de reembolso','documents':[],'rewrite_count':0})
assert s.get('documents'), s
print('ok', len(s['documents']), s['documents'][0][:80])
"
```

## Tema
Cite N3 — ingest+retrieve
