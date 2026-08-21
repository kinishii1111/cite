# Demo — Cite (5 perguntas)

Setup:

```bash
python -m cite ingest
```

## 1. Citação

```bash
python -m cite ask "Qual o prazo de reembolso e onde isso está escrito?"
```

Cita `docs/reembolso.md` (7 dias úteis).

## 2. Recusa

```bash
python -m cite ask "Qual o CNPJ da Receita Federal?"
```

**Recusa**: fora da base, não inventa.

## 3. Vaga (oferta de projeto)

```bash
python -m cite ask "Vocês atendem projetos de agente LangGraph/RAG?"
```

Cita `docs/escopo.md` e `docs/stack.md` (integração de agentes LangGraph).

## 4. Conceito

```bash
python -m cite ask "O que é RAG?"
```

`skip_retrieve`: responde direto, sem recuperar docs.

## 5. Thread

```bash
python -m cite ask --thread demo "Qual o prazo para entregar um agente LangGraph?"
python -m cite ask --thread demo "e o prazo mesmo?"
```

Mesmo `--thread demo`: a 2ª pergunta reusa o contexto da 1ª (memória de thread). Cita `docs/prazo-projeto.md` (10 a 20 dias úteis).