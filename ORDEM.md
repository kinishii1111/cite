# ORDEM — tarefa/c1-core

## Agente
opencode

## Objetivo
State + esqueleto do grafo Cite (nós stub) + placeholders CLI. Sem ingest ainda. Sem docs/.

## Copiar de
- Brief: State messages, question, documents, rewrite_count, generation
- Nós: route, retrieve, grade_docs, rewrite, generate, ground
- Recall pattern: thread_id + SqliteSaver (pode stub MemorySaver se Sqlite ainda não linkado)

## Fazer
1. `src/cite/state.py` — TypedDict/MessagesState com fields do brief
2. Stubs (funções que retornam state mínimo / placeholders):
   - route.py, retrieve.py, grade.py, rewrite.py, generate.py, ground.py
3. `src/cite/graph.py` — StateGraph ligando o fluxo do brief (mesmo com stubs); compile com checkpointer se fácil (MemorySaver ok nesta ORDEM)
4. `src/cite/cli.py` — argparse: `ingest` (print "TODO"), `ask` (invoke grafo stub), `eval` (print TODO)
5. `src/cite/__main__.py` — chama cli.main
6. NÃO tocar docs/ (outro lacaio)
7. Commit prefix: `opencode:`

## Arquivos permitidos
- src/cite/
- pyproject.toml (só se faltar script)
- ORDEM.md
- NÃO docs/ NÃO eval/

## Não fazer
- Sem chromadb real nesta ORDEM (retrieve stub)
- Sem UI / testes suite
- Sem merge main

## Ownership
- src/cite/

## Pronto quando
```bash
cd /home/kin/Documents/estudo/langgraph-portfolio/trabalho/cite
PYTHONPATH=src python3 -c "from cite.graph import build_graph; g=build_graph(); print('ok', type(g).__name__)"
PYTHONPATH=src python3 -m cite --help
```

## Tema
Cite N3 — esqueleto grafo
