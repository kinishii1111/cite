# Stack Tecnológica

Padrões de tecnologia e arquitetura adotados nos projetos KinSolo.

## Tecnologias Principais
- **n8n**: Plataforma principal de orquestração e fluxos no-code/low-code.
- **VPS Linux**: Servidores Ubuntu/Debian com Docker e Docker Compose.
- **LangGraph & Python**: Orquestração de agentes autônomos e lógica avançada de IA.
- **PostgreSQL / Redis**: Armazenamento relacional e controle de fila/estado.
- **Caddy / Nginx**: Reverse proxy com SSL automático via Let's Encrypt.

## Limites e Premissas
- Instalações são conteinerizadas via Docker para portabilidade e isolamento.
- Recursos mínimos recomendados para VPS: 2 vCPU, 4GB RAM e 40GB SSD.
- Integrações dependem da estabilidade das APIs externas dos fornecedores.
- Modelos LLM utilizam provedores externos via chave de API gerenciada pelo cliente.
