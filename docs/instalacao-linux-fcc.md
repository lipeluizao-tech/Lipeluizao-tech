# Kit gratuito para Zorin OS, projetos e Free Claude Code

Este guia reúne instalações, verificações e uma rotina noturna. Os programas sugeridos são gratuitos; APIs de IA, hospedagem, armazenamento remoto e alguns serviços podem ter custos ou limites. Nenhuma ferramenta garante precisão ou sucesso: testes, revisão e backups ajudam a avaliar resultados.

**FCC significa Free Claude Code.** O projeto público pesquisado foi [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code), cujo README já documenta Telegram nativo. O link do seu projeto ainda precisa ser confirmado; um fork antigo pode ter comandos e recursos diferentes.

Os comandos são para executar no seu computador, não foram instalados nele nesta conversa. Os exemplos pressupõem Zorin baseado em Ubuntu, Bash e Python 3.8 ou superior para o notificador. Confirme a versão e o hardware antes de instalar serviços grandes.

## 1. Ferramentas que recomendo

| Ferramenta gratuita | Benefício concreto | Uso durante a noite |
| --- | --- | --- |
| tmux | Retomar terminais e manter sessões | FCC e tarefas continuam ao fechar a janela |
| htop | Observar CPU, RAM e processos | Diagnóstico de consumo; não otimiza sozinho |
| ripgrep + fzf + jq | Buscar código, selecionar arquivos e inspecionar JSON | Consultas e automações |
| uv | Gerenciar ambientes e dependências Python | Instalação e execução reproduzível com lockfile |
| Ruff | Análise e formatação de Python | Verificações automáticas de qualidade |
| pytest | Testar comportamento do código | Testes com resultado verificável |
| ShellCheck | Detectar problemas em scripts shell | Revisão dos scripts de automação |
| pre-commit | Executar verificações antes do commit | Padronizar qualidade; depende dos hooks configurados |
| Restic | Backups com histórico e criptografia | Backup programado em destino configurado |
| Syncthing | Sincronizar arquivos entre dispositivos | Sincronização contínua; não substitui backup |
| KeePassXC | Guardar credenciais em banco criptografado | Organizar senhas e tokens localmente |
| FCC | Conectar agentes de programação aos provedores | Conversar pelo Telegram e executar tarefas delimitadas |

Comece com tmux, uv, Ruff e testes. Acrescente sincronização, backup e FCC quando houver uma necessidade concreta.

## 2. Identifique o Linux

```bash
cat /etc/os-release
uname -m
free -h
df -h "$HOME"
```

Anote versão, arquitetura e RAM. Os pacotes APT variam com a versão e seus repositórios. Consulte `apt policy nome-do-pacote` quando um pacote não for encontrado; mantenha assinaturas e TLS habilitados.

## 3. Base e ferramentas de terminal

```bash
sudo apt update
sudo apt install git curl ca-certificates build-essential python3 python3-venv pipx tmux htop ripgrep fzf jq sqlite3 shellcheck
python3 -m pipx ensurepath
```

Abra um novo terminal após `ensurepath` e verifique:

```bash
git --version
python3 --version
pipx --version
tmux -V
rg --version
shellcheck --version
```

## 4. Ferramentas Python isoladas

```bash
pipx install uv
pipx install pre-commit
uv --version
pre-commit --version
```

Se já estiverem instaladas, use `pipx upgrade uv` ou `pipx upgrade pre-commit`, conferindo a compatibilidade do projeto antes de atualizar.

Em um **projeto Python seu**, para adicionar ferramentas de qualidade:

```bash
cd ~/Projetos/meu-projeto-python
# O projeto precisa ter pyproject.toml; uv init cria um novo projeto quando necessário.
uv add --dev ruff pytest
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

`uv add` altera as dependências do projeto: revise e versione `pyproject.toml` e `uv.lock`. Em um projeto já configurado, prefira suas instruções e `uv sync --frozen`. Ruff não substitui testes; pytest sem testes coletados não valida funcionalidades.

Para scripts Bash, substitua pelo caminho real:

```bash
shellcheck caminho/do/script.sh
```

`pre-commit install` só deve ser usado em um repositório com `.pre-commit-config.yaml` escolhido e revisado. `pre-commit run --all-files` executa os hooks configurados e pode modificar arquivos; revise o diff.

## 5. Backup, sincronização e senhas

```bash
sudo apt install restic syncthing keepassxc
restic version
syncthing --version
keepassxc --version
```

**Restic:** escolha uma pasta em um disco de backup montado. Não inicialize no mesmo lugar dos arquivos originais. Os comandos abaixo pedem que você informe o caminho antes de qualquer operação:

```bash
read -r -p "Pasta do repositório de backup em disco montado: " BACKUP_REPO
: "${BACKUP_REPO:?Informe um caminho válido}"
# Apenas na primeira utilização, inicialize e escolha uma senha:
restic -r "$BACKUP_REPO" init
restic -r "$BACKUP_REPO" backup "$HOME/Projetos"
restic -r "$BACKUP_REPO" snapshots
restic -r "$BACKUP_REPO" check
```

Guarde a senha; sem ela o backup não pode ser recuperado. Para uso automático, configure um arquivo privado de senha e o destino antes de agendar. Faça uma restauração de teste para outra pasta. Não configure limpeza automática de snapshots sem definir a retenção.

**Syncthing:** emparelhe os dispositivos e selecione uma pasta de trabalho na interface. Evite sincronizar credenciais ou ambientes `.venv` e `node_modules`. Ative versionamento quando adequado; exclusões também podem ser sincronizadas.

```bash
# Confira se o pacote fornece esta unidade de usuário antes de habilitar:
systemctl --user list-unit-files 'syncthing*'
systemctl --user enable --now syncthing.service
systemctl --user status syncthing.service
```

Se a unidade não existir, use as instruções do pacote/versão ou inicie `syncthing` manualmente. Mantenha a interface administrativa restrita ao computador.

## 6. Instalação do FCC pesquisado

A versão consultada usa seu instalador oficial para preparar Python e agentes. Não substitua o Python do Zorin pela versão exigida pelo FCC. Primeiro confirme se esse repositório corresponde ao seu projeto.

Baixe o instalador do commit consultado, leia e execute no terminal:

```bash
mkdir -p "$HOME/.cache/portfolio-install"
curl --fail --location --proto '=https' --tlsv1.2 \
  'https://raw.githubusercontent.com/Alishahryar1/free-claude-code/261ecf7a181dd66098bf6fd2c2ee79a8c15d370e/scripts/install.sh' \
  -o "$HOME/.cache/portfolio-install/fcc-install.sh"
less "$HOME/.cache/portfolio-install/fcc-install.sh"
sh "$HOME/.cache/portfolio-install/fcc-install.sh" --help
sh "$HOME/.cache/portfolio-install/fcc-install.sh"
```

O instalador é interativo: escolha apenas os agentes necessários. Ele pode buscar pacotes/releases atuais; fixar a URL do script não fixa todas as dependências. As opções `--dry-run` e `--rtk-headroom` existem no instalador consultado. RTK e Headroom são opcionais; avalie os resultados antes de adotá-los.

Depois:

```bash
fcc-server --version
fcc-server
# Em outro terminal, na pasta do projeto e com o servidor ativo:
# fcc-claude
```

Abra a Admin UI indicada no log, configure seu provedor e teste uma tarefa pequena. O nome Free Claude Code não significa acesso ilimitado aos modelos Claude; disponibilidade, quotas e custos dependem do provedor escolhido.

## 7. Conversar pelo Telegram

No FCC pesquisado: **Admin UI → Messaging → Messaging Platform = telegram**.

1. No Telegram, abra o BotFather oficial, `@BotFather`, e use `/newbot`.
2. Guarde o token em local privado e cole em **Telegram Bot Token** na Admin UI.
3. Informe seu ID numérico em **Allowed Telegram User ID**. O README indica `@userinfobot` para consultar o ID; use apenas esse dado, nunca envie tokens a outros bots.
4. Em **Allowed Directory**, coloque a pasta absoluta de um projeto dedicado, por exemplo `/home/seu-usuario/Projetos/projeto-teste`.
5. Clique **Apply**, reinicie se solicitado e envie `/start` ao seu bot para abrir a conversa.
6. Envie uma tarefa pequena, como pedir a descrição do projeto, e confira a resposta.

O FCC deve permanecer ativo e conectado. Os comandos documentados incluem `/stats`, `/stop` e `/clear`. Mantenha as permissões do agente limitadas ao trabalho escolhido; não habilite execução irrestrita para tarefas noturnas.

**BotFather é do Telegram.** Se “Facebook admin” significar uma Página no Facebook, essa é outra integração: depende de aplicativo Meta, permissões da Página, credenciais e webhook HTTPS. Isso ainda precisa ser esclarecido; nenhuma integração Meta foi ativada.

## 8. Receber aviso de término pelo Telegram

O arquivo `scripts/notificar_telegram.py` deste kit executa um comando local, grava um log privado e envia uma notificação ao terminar. Ele pode usar o mesmo bot do FCC porque só chama `sendMessage`, sem disputar o recebimento das mensagens.

Primeiro extraia o ZIP ou clone o portfólio:

```bash
mkdir -p "$HOME/Projetos"
cd "$HOME/Projetos"
git clone https://github.com/lipeluizao-tech/Lipeluizao-tech.git
cd Lipeluizao-tech
```

Se o repositório já existir, use sua cópia e atualize com `git pull --ff-only` após revisar o estado local.

Crie uma configuração privada fora do repositório:

```bash
mkdir -p "$HOME/.config/portfolio"
chmod 700 "$HOME/.config/portfolio"
# Na primeira vez; -i pergunta antes de sobrescrever uma configuração existente.
cp -i config/telegram.json.example "$HOME/.config/portfolio/telegram.json"
chmod 600 "$HOME/.config/portfolio/telegram.json"
nano "$HOME/.config/portfolio/telegram.json"
```

Preencha `bot_token` e `chat_id` apenas nessa cópia. Para uma conversa privada com você, o `chat_id` normalmente corresponde ao seu ID numérico; em grupos é outro ID. Inicie a conversa com o bot antes de testar. Nunca envie o token nesta conversa nem faça commit dele.

```bash
python3 scripts/notificar_telegram.py \
  --config "$HOME/.config/portfolio/telegram.json" \
  --message "Notificações do meu Linux configuradas."
```

Para rodar testes do seu projeto com limite de duas horas e aviso de resultado:

```bash
python3 "$HOME/Projetos/Lipeluizao-tech/scripts/notificar_telegram.py" \
  --config "$HOME/.config/portfolio/telegram.json" \
  --cwd "$HOME/Projetos/meu-projeto-python" \
  --timeout 7200 --title "Testes do projeto" \
  --run uv run pytest
```

Troque a pasta e o comando pelos reais. O comando recebe argumentos diretamente, sem interpretação shell; não use pipes ou `&&` nesse campo. Para um fluxo composto, use um script local que preserve o resultado de cada etapa.

Resultado 0 significa sucesso do comando; outros códigos indicam falha, 124 indica limite de tempo e 127 falha ao iniciar. A mensagem inclui estado, duração e caminho do log. Não envia conteúdo dos logs nem argumentos do comando. Se o Telegram falhar, mostra um aviso e preserva o resultado da tarefa. Logs ficam em `~/.local/state/portfolio/logs`; monitore espaço e remova arquivos antigos quando apropriado.

## 9. Manter o trabalho durante a noite

```bash
tmux new -s noite
systemd-inhibit --what=sleep --mode=block --why="Trabalho noturno" bash
# Neste shell, execute fcc-server OU o comando de tarefa escolhido.
# Para outra tarefa, crie outra janela do tmux: Ctrl+b, depois c.
```

Desconecte com **Ctrl+b, depois d**; retorne com `tmux attach -t noite`. O `systemd-inhibit` vale somente enquanto o comando associado estiver ativo. Para manter o FCC sem suspensão, você pode executar diretamente `systemd-inhibit --what=sleep --mode=block --why="FCC ativo" fcc-server` na janela correspondente.

Fechar a janela não é o mesmo que desligar, suspender ou reiniciar o PC. Ajustes ao fechar a tampa dependem do sistema. Garanta alimentação, ventilação e espaço livre. Faça um primeiro ciclo curto, confira resposta do Telegram, limite de tempo e consumo antes de deixar tarefas longas.

Os programas só trabalham quando têm tarefas configuradas; deixá-los abertos não melhora código automaticamente. Defina entregas, limites de tempo, testes e revisão das mudanças. Não repita chamadas de IA indefinidamente: respeite quotas e custos.

## 10. Validação do kit

Sem tokens e sem mensagens externas, na pasta do kit:

```bash
python3 -m unittest discover -s tests -v
python3 scripts/notificar_telegram.py --help
```

Foram executados testes locais de envio simulado, falhas, timeout, preservação de status e logs privados. A comunicação real com Telegram, o FCC do usuário e o Zorin precisam de configuração e validação no seu computador.

## Fontes

READMEs consultados: [FCC](https://github.com/Alishahryar1/free-claude-code), [uv](https://github.com/astral-sh/uv), [Ruff](https://github.com/astral-sh/ruff), [pytest](https://github.com/pytest-dev/pytest), [pre-commit](https://github.com/pre-commit/pre-commit), [Restic](https://github.com/restic/restic) e [Syncthing](https://github.com/syncthing/syncthing). Os commits estão em `referencias/fontes.json` no kit. Veja também a [ajuda oficial do Zorin](https://help.zorin.com/) e a [API de bots do Telegram](https://core.telegram.org/bots/api).
