# Segurança e Gestão de Segredos

Políticas de proteção de credenciais, chaves de API e privacidade na KinSolo.

## Gestão de Variáveis e Segredos
- Todas as credenciais de produção devem residir exclusivamente em arquivos `.env` ou no cofre de credenciais nativo do n8n.
- Arquivos `.env`, chaves privadas SSH e tokens de API **nunca** são commitados em repositórios Git.
- Todos os repositórios contam com `.gitignore` configurado estritamente para bloquear vazamento de segredos.

## Infraestrutura e Acesso
- Acesso SSH a servidores VPS restrito a autenticação por par de chaves criptográficas (sem senha).
- Portas não essenciais bloqueadas via firewall UFW no servidor Linux.
- Certificados SSL/TLS obrigatórios e renovados automaticamente para todas as rotas públicas.
