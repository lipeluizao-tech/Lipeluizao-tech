# Notificador Telegram de tarefas locais

## Objetivo e estado

Receber no Telegram o resultado de tarefas de desenvolvimento executadas no Linux. Implementado neste repositório em [scripts/notificar_telegram.py](../scripts/notificar_telegram.py); envio real depende da configuração privada do usuário.

## Tecnologias

Python 3.8 ou superior, biblioteca padrão, Telegram Bot API e subprocessos POSIX. Sem pacotes Python externos. O FCC pesquisado cuida da conversa com a IA; este script envia avisos de tarefas locais.

## Execução

O [kit](../docs/instalacao-linux-fcc.md) explica configuração, teste de mensagem e execução de comandos. Token e chat ID ficam fora do checkout.

## Verificação

`python3 -m unittest discover -s tests -v`: 11 testes locais aprovados, com Telegram simulado e subprocessos reais. Cobrem sucesso, erro, timeout, configuração, preservação de código de saída e proteção de logs. Não houve envio real ao usuário.

## Decisões

Execução sem shell para preservar a separação dos argumentos. Timeout para limitar tarefas noturnas. Logs 0600 e mensagem sem trechos da saída ou argumentos. O código de saída do comando é preservado mesmo se o Telegram falhar.

## Limitações

Requer Linux e conectividade para notificações. Não reinicia tarefas após reboot, não mantém o PC acordado e não repete automaticamente mensagens que falham. Cada execução é independente; não há contexto de conversa da IA neste script. Logs precisam de manutenção de espaço.

## Referências

[Free Claude Code](https://github.com/Alishahryar1/free-claude-code) para a configuração nativa e [Telegram Bot API](https://core.telegram.org/bots/api) para notificações. O script foi criado para este portfólio; o FCC é um projeto de terceiros.
