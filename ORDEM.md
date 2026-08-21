# ORDEM — tarefa/c7-trace

## Agente
agy

## Objetivo
`cite ask` imprime meta de roteamento (trace mínimo): skip_retrieve + rewrite_count. Sem mudar grafo.

## Copiar de
- `src/cite/cli.py` atual — só estender print
- `src/cite/state.py` — campos `skip_retrieve`, `rewrite_count`

## Fazer
1. Após `graph.invoke`, além de `generation`, imprimir em stderr (ou stdout após a resposta) uma linha:
   `trace: skip_retrieve=… rewrite_count=…`
2. Valores vêm do `result` do invoke
3. Commit `agy:`
4. NÃO: graph.py, eval/, memory.py, README

## Arquivos permitidos
- src/cite/cli.py
- ORDEM.md

## Ownership
- src/cite/cli.py

## Pronto quando
```bash
cd /home/kin/Documents/estudo/langgraph-portfolio/trabalho/cite-wt-tarefa-c7-trace
grep -q 'rewrite_count\|skip_retrieve' src/cite/cli.py
grep -q 'trace:' src/cite/cli.py
```

## Tema
Cite — trace CLI
