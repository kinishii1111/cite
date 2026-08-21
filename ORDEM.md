# ORDEM — tarefa/c1-docs

## Agente
agy

## Objetivo
Corpus KinSolo Handbook: 10 markdowns em docs/ para Cite (RAG). Tema: empresa solo de automação (n8n/VPS). Sintético de propósito.

## Copiar de
- entrada brief: política comercial / FAQ produto solo
- Nada de PDF da internet

## Fazer
1. Criar exatamente estes arquivos (PT-BR, curtos, 15–40 linhas cada):
   - docs/README.md — índice do corpus
   - docs/reembolso.md — prazo reembolso 7 dias úteis, como pedir, o que não cobre
   - docs/escopo.md — o que a KinSolo faz / não faz
   - docs/stack.md — n8n, VPS, LangGraph, limites
   - docs/prazo-projeto.md — prazos típicos de entrega
   - docs/suporte.md — horário, canais, SLA
   - docs/precos.md — faixas (sem inventar CNPJ/Receita)
   - docs/onboarding.md — kickoff cliente
   - docs/seguranca.md — segredos, .env, o que não commitamos
   - docs/faq.md — 5 FAQs curtas
2. Em reembolso.md: seção clara "Prazo" com "7 dias úteis" (ouro do brief)
3. NÃO criar código Python

## Arquivos permitidos
- docs/
- ORDEM.md
- NÃO abrir mais nada

## Não fazer
- Sem UI / chromadb / src/ / eval /
- Sem inventar CNPJ da Receita Federal em lugar nenhum

## Ownership
- docs/

## Pronto quando
```bash
test -f docs/reembolso.md && grep -q '7 dias' docs/reembolso.md && test $(ls docs/*.md | wc -l) -ge 10 && echo docs_ok
```

## Tema
Cite N3 — corpus KinSolo
