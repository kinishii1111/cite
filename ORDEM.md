# ORDEM — tarefa/c4-readme

## Agente
agy

## Objetivo
README de portfólio + diagrama do grafo Cite. Sem mudar lógica LLM. Sem Desk.

## Copiar de
- Brief N3: por que Agentic RAG ≠ `similarity_search` + LLM; critérios de pronto; linha de currículo
- `src/cite/graph.py` — nós e arestas reais (route → retrieve|generate → grade → rewrite|generate → ground)
- `eval/golden.json` — score 6/6 (ou “6 casos, ≥70%”) pra citar no README
- ToolSmith README (`../toolsmith/README.md` se existir no sibling) — tom curto, demo CLI
- Corpus: `docs/` = KinSolo Handbook (sintético — declarar no README)

## Fazer
1. `diagrams/graph.mmd` — Mermaid do grafo **como está no código**:
   - START → route
   - route -->|skip_retrieve| generate
   - route -->|else| retrieve → grade_docs
   - grade_docs -->|docs ok| generate
   - grade_docs -->|sem docs & rewrite_count < 2| rewrite → retrieve
   - grade_docs -->|sem docs & rewrite_count ≥ 2| generate
   - generate → ground → END
2. `README.md` — em PT, curto (≤ ~120 linhas), seções:
   - O que é (1 parágrafo) + linha de currículo
   - Por que Agentic ≠ similarity + LLM (3–5 bullets)
   - Grafo (link/embed do `diagrams/graph.mmd`)
   - Setup: `pip install -e .`, `.env` (`GROQ_API_KEY`), `CITE_EMBED=default` (ONNX) / `hf` na VM
   - CLI: `python -m cite ingest` · `ask "..."` · `eval`
   - Demo 4 comandos (reembolso / CNPJ / “o que é RAG?” / eval)
   - Corpus: KinSolo sintético, propositalmente pequeno
   - Eval: golden ≥6, threshold 70%
   - Fora de escopo: UI, Desk multi-agente, web search no generate
3. Commit prefix: `agy:`
4. NÃO: mudar `src/cite/*` (exceto se README mentir — aí BLOQUEIO, não “consertar” grafo)
5. NÃO: pytest, UI, Desk, torch

## Arquivos permitidos
- README.md
- diagrams/graph.mmd
- ORDEM.md
- examples/demo.md (opcional, 1 página com os 4 asks)

## Ownership
- README.md
- diagrams/
- examples/ (se criar)

## Não fazer
- Mexer `src/`, `eval/golden.json`, `docs/` conteúdo
- Merge main
- Inventar features que o código não tem (ex.: SqliteSaver se ainda é MemorySaver — diga a verdade: MemorySaver agora)

## Pronto quando
```bash
cd /home/kin/Documents/estudo/langgraph-portfolio/trabalho/cite-wt-tarefa-c4-readme
test -f README.md && test -f diagrams/graph.mmd
grep -q 'Agentic' README.md
grep -q 'skip_retrieve\|route' diagrams/graph.mmd
grep -q 'python -m cite' README.md
grep -q 'KinSolo\|sintético\|sintetico' README.md
# diagrama menciona os nós reais
grep -E 'grade_docs|rewrite|ground' diagrams/graph.mmd
```

## Tema
Cite N3 — README + diagrama (fechamento brief)
