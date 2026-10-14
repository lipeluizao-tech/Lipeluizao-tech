#!/usr/bin/env python3
"""Notificações pessoais de tarefas locais; usa somente a biblioteca padrão."""

import argparse
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request


class NotificationError(Exception):
    """Erro seguro para exibir sem revelar o token ou a URL autenticada."""


def load_config(config_path=None):
    config = {}
    if config_path:
        try:
            config = json.loads(Path(config_path).expanduser().read_text())
        except (OSError, ValueError) as exc:
            raise NotificationError("Não foi possível ler o arquivo JSON de configuração.") from exc
        if not isinstance(config, dict):
            raise NotificationError("A configuração precisa ser um objeto JSON.")
    token = os.environ.get("TELEGRAM_BOT_TOKEN") or config.get("bot_token", "")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID") or config.get("chat_id", "")
    if not isinstance(token, str) or not re.fullmatch(r"[0-9]+:[A-Za-z0-9_-]{20,}", token):
        raise NotificationError("Configure um token válido do BotFather em arquivo privado ou variável local.")
    if not re.fullmatch(r"-?[0-9]+", str(chat_id)) or int(chat_id) == 0:
        raise NotificationError("Configure TELEGRAM_CHAT_ID ou chat_id com o ID numérico da conversa.")
    return token, str(chat_id)


def send_message(token, chat_id, message):
    if not message or len(message) > 3500:
        raise NotificationError("A mensagem precisa ter entre 1 e 3500 caracteres.")
    payload = json.dumps({"chat_id": chat_id, "text": message}).encode("utf-8")
    request = urllib.request.Request(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            result = json.loads(response.read())
    except urllib.error.HTTPError as exc:
        raise NotificationError(f"Telegram recusou a notificação (HTTP {exc.code}).") from exc
    except (urllib.error.URLError, OSError, ValueError) as exc:
        raise NotificationError("Falha de conexão ou resposta inválida do Telegram.") from exc
    if not isinstance(result, dict) or result.get("ok") is not True:
        raise NotificationError("Telegram não confirmou o envio da notificação.")


def stop_process_group(process):
    # start_new_session cria um grupo separado: também encerra filhos no timeout.
    try:
        os.killpg(process.pid, signal.SIGTERM)
    except ProcessLookupError:
        pass
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        pass
    finally:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        process.wait()


def run_job(command, cwd, timeout, log_path):
    with open(log_path, "ab") as log:
        try:
            process = subprocess.Popen(
                command,
                cwd=cwd,
                stdin=subprocess.DEVNULL,
                stdout=log,
                stderr=subprocess.STDOUT,
                start_new_session=True,
            )
        except OSError:
            log.write(b"Nao foi possivel iniciar o comando.\n")
            return 127
        try:
            code = process.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            stop_process_group(process)
            log.write(b"\nTarefa encerrada pelo limite de tempo.\n")
            return 124
        except KeyboardInterrupt:
            stop_process_group(process)
            return 130
    return code if code >= 0 else 128 - code


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", help="Arquivo JSON privado (não versionar).")
    parser.add_argument("--cwd", default=".", help="Pasta de trabalho do comando.")
    parser.add_argument("--timeout", type=int, default=7200, help="Limite de tempo em segundos.")
    parser.add_argument("--title", default="Tarefa de desenvolvimento", help="Nome curto da tarefa.")
    parser.add_argument("--log-dir", default="~/.local/state/portfolio/logs")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--message", help="Enviar uma mensagem de teste ou aviso manual.")
    mode.add_argument("--run", nargs=argparse.REMAINDER, help="Executar comando sem shell e avisar ao terminar.")
    args = parser.parse_args(argv)
    if args.timeout <= 0:
        parser.error("--timeout deve ser positivo")
    if not args.title.strip() or len(args.title) > 200:
        parser.error("--title deve conter entre 1 e 200 caracteres")
    command = args.run
    if command and command[0] == "--":
        command = command[1:]
    if args.run is not None and not command:
        parser.error("informe o comando depois de --run")
    try:
        token, chat_id = load_config(args.config)
        if args.message is not None:
            send_message(token, chat_id, args.message)
            print("Telegram confirmou o envio da mensagem.")
            return 0
        cwd = Path(args.cwd).expanduser().resolve()
        if not cwd.is_dir():
            raise NotificationError("A pasta de trabalho não existe.")
        log_dir = Path(args.log_dir).expanduser()
        log_dir.mkdir(parents=True, mode=0o700, exist_ok=True)
        fd, filename = tempfile.mkstemp(prefix="tarefa-", suffix=".log", dir=log_dir)
        os.close(fd)  # mkstemp cria arquivo com permissões 0600.
        started = time.monotonic()
        code = run_job(command, str(cwd), args.timeout, filename)
        duration = round(time.monotonic() - started)
        state = "CONCLUÍDA" if code == 0 else "FALHOU"
        if code == 124:
            state = "LIMITE DE TEMPO"
        message = f"{args.title}: {state}\nCódigo: {code}\nDuração: {duration}s\nLog local: {filename}"
        print(message)
        try:
            send_message(token, chat_id, message)
        except NotificationError as exc:
            # Um problema no Telegram não altera o resultado dos testes/comando.
            print(f"Aviso: {exc} O resultado da tarefa foi preservado.", file=sys.stderr)
        return code
    except (NotificationError, OSError) as exc:
        message = str(exc) if isinstance(exc, NotificationError) else "Falha ao preparar os arquivos locais."
        print(message, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
