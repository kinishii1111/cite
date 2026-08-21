# ORDEM — tarefa/c5-eval8

## Agente
opencode

## Objetivo
Golden eval ≥8 casos + runner já existente. Score impresso. Sem mexer no grafo.

## Copiar de
- `eval/golden.json` atual (6 casos) — manter ids c1–c6; adicionar c7+
- Brief N3: ≥8; tipos cite / refuse / skip_retrieve
- `eval/run.py` — threshold 70%; classificador já existe

## Fazer
1. `eval/golden.json` → **≥8** casos. Obrigatórios além dos 6:
   - c7: pergunta vaga tipo “e o prazo?” → expect `cite` ou o que o pipeline fizer de forma estável (se flaky, `cite` com pergunta um pouco mais específica sobre reembolso)
   - c8: “O que é LangGraph?” → `skip_retrieve`
2. `eval/run.py` — ao final imprimir linha `SCORE: X/Y (Z%)` (além do que já tem)
3. Commit `opencode:`
4. NÃO: src/, README, docs/, diagrams/

## Arquivos permitidos
- eval/golden.json
- eval/run.py
- ORDEM.md

## Ownership
- eval/

## Pronto quando
```bash
cd /home/kin/Documents/estudo/langgraph-portfolio/trabalho/cite-wt-tarefa-c5-eval8
python3 -c "import json; a=json.load(open('eval/golden.json')); assert len(a)>=8, len(a)"
grep -q 'SCORE:' eval/run.py
# com GROQ (se .env): PYTHONPATH=src python3 -m cite eval ; echo exit=$?
```

## Tema
Cite — eval 8+
