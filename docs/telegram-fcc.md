# Telegram e Free Claude Code

FCC foi identificado pelo usuário como **Free Claude Code**. O link do projeto específico ainda não foi informado. A referência pesquisada é [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code), que documenta integração nativa com Telegram na Admin UI.

## Conversa com a IA

Use **Admin UI → Messaging → telegram**, configurando token do BotFather, seu ID numérico autorizado e uma pasta absoluta de projeto. Clique Apply e faça uma conversa de teste com o FCC ativo. Os detalhes estão no [kit de instalação](instalacao-linux-fcc.md).

O bot é criado pelo **BotFather**. A expressão “Facebook admin” ainda precisa de confirmação: uma Página no Facebook exigiria integração separada com a plataforma Meta. Nenhum aplicativo Meta ou webhook foi criado.

## Avisos de tarefas

O [notificador](../scripts/notificar_telegram.py) acrescenta avisos pessoais ao término de comandos locais: testes, builds ou outras tarefas escolhidas pelo usuário. Ele não recebe ordens do Telegram e não substitui o bot nativo do FCC.

- Configuração por arquivo JSON privado ou variáveis `TELEGRAM_BOT_TOKEN` e `TELEGRAM_CHAT_ID`.
- Sem dependências Python externas; usa a biblioteca padrão no Linux.
- Execução por lista de argumentos, sem shell, com timeout e log privado.
- Envio apenas do estado, duração, código de saída e caminho do log.
- Falha de notificação não altera o código de saída da tarefa.

Consulte [configuração e comandos](instalacao-linux-fcc.md) e o [exemplo sem credenciais](../config/telegram.json.example).

## Estado de validação

Os [testes locais](../tests/test_notificar_telegram.py) verificam comportamento do notificador sem mensagens externas. Não houve conexão ao seu Telegram, instalação no seu computador ou validação de seu FCC. Para ativar, configure as credenciais localmente e teste o envio. Não compartilhe tokens pelo chat ou GitHub.
