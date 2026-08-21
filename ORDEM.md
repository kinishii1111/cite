# ORDEM — tarefa/c8-examples

## Agente
grok

## Objetivo
`examples/demo.md` — 5 comandos demo do brief (citação, recusa, vaga, conceito, thread). Só markdown.

## Copiar de
- Brief N3 “Demo obrigatória (5 perguntas)”
- `README.md` seção CLI (comandos reais: `python -m cite ask` / `ingest` / `eval`)
- NÃO inventar flags que não existem (ex.: se não houver `--verbose`, não documentar)

## Fazer
1. Criar `examples/demo.md` com:
   - setup 1 linha (ingest)
   - 5 asks numerados alinhados ao brief
   - nota: thread = `--thread demo` duas vezes (2ª pergunta “e o prazo mesmo?”)
2. Commit `grok:`
3. NÃO: src/, eval/, README.md

## Arquivos permitidos
- examples/demo.md
- ORDEM.md

## Ownership
- examples/

## Pronto quando
```bash
cd /home/kin/Documents/estudo/langgraph-portfolio/trabalho/cite-wt-tarefa-c8-examples
test -f examples/demo.md
grep -c 'python -m cite' examples/demo.md | grep -E '^[5-9]|^[0-9]{2}'
grep -q 'thread' examples/demo.md
grep -q 'reembolso\|reembolso\|CNPJ\|LangGraph\|RAG' examples/demo.md
```

## Tema
Cite — examples demo
