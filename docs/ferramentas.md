# Ferramentas e migração para Linux

Ambiente informado: Zorin OS. As ferramentas anteriores ainda não foram informadas; estas opções são sugestões, não um inventário confirmado de instalações.

Veja também o [kit com comandos de instalação](instalacao-linux-fcc.md), incluindo uv, Ruff, pytest, ShellCheck, Restic, Syncthing, KeePassXC e Telegram.

## Base sugerida

| Necessidade | Opção no Linux | Uso | Como conferir |
| --- | --- | --- | --- |
| Editor | VS Code ou VSCodium | Código, depuração e extensões | Abrir e executar um projeto |
| Versionamento | Git | Histórico e colaboração | `git --version` e `git status` |
| Python | Python 3 + venv | Automação, APIs e experimentos | Criar ambiente e executar testes do projeto |
| JavaScript/TypeScript | Node.js via nvm | Web e ferramentas | `node --version`, `npm --version` e testes |
| Terminal | tmux | Retomar sessões | Criar, desconectar e reconectar |
| Monitoramento | htop | Observar CPU e memória | `htop` |
| Busca em código | ripgrep | Procurar texto | `rg --version` |
| Containers, quando necessários | Docker + Compose | Serviços reproduzíveis | Verificação documentada do projeto |
| HTTP e APIs | curl; interface gráfica opcional | Testar endpoints | Requisição à própria aplicação |
| Segurança de código | Semgrep | Encontrar padrões e revisar riscos | Executar regra local e revisar achados |
| HTTP de laboratório | mitmproxy | Entender tráfego | Usar com aplicação própria e dados fictícios |
| IA, quando necessária | Ollama, llama.cpp ou serviço remoto | Inferência e experimentos | Tarefa pequena com tempo e resultado registrados |

O [guia do Zorin](zorin-os.md) contém a preparação inicial. As referências de segurança e IA estão no [catálogo](repositorios.md). Hardware, versões e custos precisam ser considerados antes de instalar modelos ou serviços grandes.

## Inventário da migração

Preencha com ferramentas reais, sem senhas ou tokens:

| Ferramenta anterior | Finalidade | Equivalente Linux | Configuração a migrar | Estado e evidência |
| --- | --- | --- | --- | --- |
| A informar | A informar | A avaliar | Extensões, atalhos ou arquivos sem segredos | Pendente |

Estados: pendente, instalada, configurada, validada, substituída. “Validada” exige uma operação real, não apenas o ícone do aplicativo.

## Informações do computador a registrar

- Versão do Zorin e base Ubuntu.
- Arquitetura, RAM e espaço disponível.
- GPU e driver, se houver objetivo de IA local.
- Linguagens prioritárias e ferramentas anteriores.

Não marque ferramentas sugeridas como tecnologias dominadas no perfil antes de usá-las em projetos.
