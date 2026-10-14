# Instruções para manutenção do portfólio

- Escreva documentação em português do Brasil com links internos relativos.
- Não invente experiência, domínio de ferramentas, projetos concluídos ou testes aprovados.
- Novos projetos reais devem ter ficha baseada em `templates/projeto.md` e entrada em `projetos/README.md`.
- Atualize documentação quando entregas mudarem; diferencie ideias, implementação, publicação e validação.
- Cite fontes externas e versões quando possível. Não apresente projetos externos como autoria própria.
- Não adicione senhas, tokens, arquivos privados ou valores reais de configuração sensível.
- Este repositório documenta o perfil. Aplicações podem ter repositórios próprios, ligados no catálogo.
- Em tarefas na nuvem, use o checkout existente. Cada tarefa já tem ambiente isolado; não crie Git worktrees sem pedido explícito.
- O guia do Zorin descreve operações no computador do usuário. Execução na nuvem não instala programas no computador dele.
- FCC significa Free Claude Code. Confirme o repositório e a versão do usuário antes de adaptar integrações; a referência pública pesquisada não prova qual fork ele usa.
- Para documentação, verifique links internos, estrutura de arquivos, JSON e `git diff --check`. Não instale dependências de aplicações apenas para editar texto.
- O notificador tem testes locais em `tests`; execute `python3 -m unittest discover -s tests -v` ao alterá-lo. Nunca use credenciais reais nos testes.
