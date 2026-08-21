# ORDEM — tarefa/c3-llm

## Agente
opencode

## Objetivo
Nós LLM do Cite (grade / rewrite / generate / ground) + arestas condicionais + eval mínima golden. Groq (`langchain-groq`). Sem UI. Sem Desk.

## Copiar de
- ToolSmith: `ChatGroq(model="openai/gpt-oss-20b")` + `GROQ_API_KEY` (não inventar model id morto)
- Brief Cite: route → retrieve → grade → rewrite (máx 2) → generate → ground; citações; recusa fora da base
- Stubs já em `src/cite/{grade,rewrite,generate,ground,route,graph,cli}.py`
- Ingest/retrieve já na main — **não reescrever** ingest/embeddings/retrieve (só chamar)

## Fazer
1. `src/cite/llm.py` — helper: `get_llm()` → ChatGroq temp=0; sem `GROQ_API_KEY` → raise RuntimeError clara (mensagem cita a env). `load_dotenv()` ok.
2. `grade.py` — LLM (ou heurística+LLM): para cada doc, relevante à `question`? Manter só relevantes em `documents`. Se nenhum → `documents=[]`.
3. `rewrite.py` — reescreve `question` para busca melhor; `rewrite_count += 1`. Se `rewrite_count >= 2` e ainda sem docs úteis: **não** loop infinito — setar `documents=[]` e deixar fluxo ir a generate (recusa).
4. `generate.py` — com docs: resposta em PT + **citação** (`source` / trecho). Sem docs: recusa explícita (“não encontrei na base KinSolo”) — **proibido inventar** fato (CNPJ, etc.).
5. `ground.py` — checa se `generation` está ancorada nos `documents`. Se alucinou: ou reescreve flag para rewrite **ou** substitui generation por recusa. Preferir recusa se `rewrite_count >= 2`.
6. `graph.py` — arestas reais:
   - `route` → se `skip_retrieve` → `generate`; senão → `retrieve`
   - `retrieve` → `grade_docs`
   - `grade_docs` → docs ok → `generate`; senão → `rewrite` (se `rewrite_count < 2`) senão → `generate`
   - `rewrite` → `retrieve`
   - `generate` → `ground` → END
7. `route.py` — manter heurística ok: conceito geral (“o que é langgraph/rag”) → `skip_retrieve=True`; pergunta factual com `?` → retrieve. Pode melhorar levemente; sem LLM obrigatório no route.
8. `cli.py` — `ask` imprime `generation` (e citations se houver). Sem key → exit 1 com msg clara. `eval` chama runner.
9. `eval/golden.json` — **≥ 6** casos (id, question, expect: `cite`|`refuse`|`skip_retrieve`). Incluir: prazo reembolso (cite); CNPJ Receita (refuse); “o que é RAG?” (skip_retrieve).
10. `eval/run.py` — roda golden via grafo; imprime PASS/FAIL; exit 0 se ≥70% pass (com GROQ). `python -m cite eval` delega pra isso.
11. `.env.example` — `GROQ_API_KEY=`
12. Commit prefix: `opencode:`
13. NÃO: UI, Desk, torch/HF, README longo, suite pytest

## Arquivos permitidos
- src/cite/llm.py (criar)
- src/cite/grade.py
- src/cite/rewrite.py
- src/cite/generate.py
- src/cite/ground.py
- src/cite/graph.py
- src/cite/route.py
- src/cite/cli.py
- src/cite/state.py (só se precisar de campo extra, ex. `skip_retrieve` já existe)
- eval/golden.json
- eval/run.py
- .env.example
- ORDEM.md
- pyproject.toml (só se faltar dep já listada — langchain-groq já está)

## Ownership
- src/cite/llm.py
- src/cite/grade.py
- src/cite/rewrite.py
- src/cite/generate.py
- src/cite/ground.py
- src/cite/graph.py
- src/cite/route.py
- src/cite/cli.py
- eval/

## Não fazer
- Mexer `ingest.py` / `embeddings.py` / `retrieve.py` / `docs/`
- Merge na main
- Hardcode de API key
- Model id inventado (usar `openai/gpt-oss-20b` como ToolSmith)

## Pronto quando
```bash
cd /home/kin/Documents/estudo/langgraph-portfolio/trabalho/cite-wt-tarefa-c3-llm
# precisa GROQ_API_KEY no ambiente ou .env local (não commitar .env)
test -n "$GROQ_API_KEY" || { echo "faltou GROQ_API_KEY"; exit 1; }
PYTHONPATH=src python3 -m cite ingest
PYTHONPATH=src python3 -m cite ask "Qual o prazo de reembolso e onde isso está escrito?"
# generation deve mencionar 7 dias e/ou reembolso.md
PYTHONPATH=src python3 -m cite ask "Qual o CNPJ da Receita Federal?"
# generation deve recusar / não inventar CNPJ
PYTHONPATH=src python3 -m cite eval
# imprime PASS/FAIL; exit 0 se score ok
```

Sem key:
```bash
GROQ_API_KEY= PYTHONPATH=src python3 -m cite ask "teste" ; test $? -ne 0
```

## Tema
Cite N3 — nós LLM + eval mínima
