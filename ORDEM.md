# ORDEM — tarefa/c6-sqlite

## Agente
opencode

## Objetivo
Trocar MemorySaver por SqliteSaver (padrão ToolSmith). Persistência por `--thread`.

## Copiar de
- **ToolSmith** `trabalho/toolsmith/src/toolsmith/memory.py` — copiar lógica `get_checkpointer` / `DEFAULT_DB`
- `src/cite/graph.py` — só trocar checkpointer no `compile`
- NÃO reinventar API LangGraph

## Fazer
1. Criar `src/cite/memory.py` espelhando ToolSmith (paths Cite: `data/checkpoints.sqlite`)
2. `graph.py` — `compile(checkpointer=get_checkpointer())` (import de `cite.memory`)
3. `.gitignore` — adicionar `data/checkpoints.sqlite` e `data/*.sqlite` se faltar
4. `pyproject.toml` — garantir dep `langgraph-checkpoint-sqlite` se ToolSmith usa (ver pyproject do toolsmith)
5. Commit `opencode:`
6. NÃO: cli.py, eval/, README, docs/

## Arquivos permitidos
- src/cite/memory.py
- src/cite/graph.py
- .gitignore
- pyproject.toml
- ORDEM.md

## Ownership
- src/cite/memory.py
- src/cite/graph.py
- .gitignore
- pyproject.toml

## Pronto quando
```bash
cd /home/kin/Documents/estudo/langgraph-portfolio/trabalho/cite-wt-tarefa-c6-sqlite
test -f src/cite/memory.py
grep -q 'SqliteSaver\|get_checkpointer' src/cite/graph.py
grep -q 'checkpoints' .gitignore
PYTHONPATH=src python3 -c "from cite.graph import build_graph; g=build_graph(); print('ok', type(g))"
```

## Tema
Cite — SqliteSaver (Recall pattern)
