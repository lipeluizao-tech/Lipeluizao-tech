"""Testes locais: nenhuma mensagem é enviada ao Telegram."""

import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import urllib.error


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "notificar_telegram.py"
SPEC = importlib.util.spec_from_file_location("notifier", SCRIPT)
notifier = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(notifier)
FAKE_TOKEN = "123456:" + "x" * 30


class TelegramTests(unittest.TestCase):
    def test_post_sends_plain_text_to_configured_chat(self):
        response = io.BytesIO(b'{"ok":true}')
        with patch.object(notifier.urllib.request, "urlopen", return_value=response) as mock:
            notifier.send_message(FAKE_TOKEN, "42", "Terminou & passou")
        request = mock.call_args.args[0]
        self.assertEqual(request.get_method(), "POST")
        self.assertEqual(json.loads(request.data), {"chat_id": "42", "text": "Terminou & passou"})
        self.assertEqual(mock.call_args.kwargs["timeout"], 30)

    def test_http_error_never_reveals_token(self):
        error = urllib.error.HTTPError(f"https://api.telegram.org/bot{FAKE_TOKEN}/sendMessage", 403, "denied", {}, None)
        with patch.object(notifier.urllib.request, "urlopen", side_effect=error):
            with self.assertRaises(notifier.NotificationError) as caught:
                notifier.send_message(FAKE_TOKEN, "42", "Aviso")
        self.assertNotIn(FAKE_TOKEN, str(caught.exception))
        self.assertIn("403", str(caught.exception))

    def test_api_rejection_is_not_success(self):
        with patch.object(notifier.urllib.request, "urlopen", return_value=io.BytesIO(b'{"ok":false}')):
            with self.assertRaises(notifier.NotificationError):
                notifier.send_message(FAKE_TOKEN, "42", "Aviso")

    def test_missing_credentials_stop_before_command(self):
        with patch.dict(os.environ, {}, clear=True), patch.object(notifier, "run_job") as run:
            with contextlib.redirect_stderr(io.StringIO()):
                code = notifier.main(["--run", sys.executable, "-c", "print('nunca')"])
        self.assertEqual(code, 2)
        run.assert_not_called()

    def test_file_configuration_and_environment_override(self):
        with tempfile.TemporaryDirectory() as directory:
            config = Path(directory) / "telegram.json"
            config.write_text(json.dumps({"bot_token": FAKE_TOKEN, "chat_id": "42"}))
            with patch.dict(os.environ, {}, clear=True):
                self.assertEqual(notifier.load_config(config), (FAKE_TOKEN, "42"))
            with patch.dict(os.environ, {"TELEGRAM_CHAT_ID": "43"}, clear=True):
                self.assertEqual(notifier.load_config(config), (FAKE_TOKEN, "43"))

    def test_success_logs_stdout_and_respects_cwd(self):
        with tempfile.TemporaryDirectory() as directory:
            log = Path(directory) / "log"
            code = notifier.run_job([sys.executable, "-c", "import os; print(os.getcwd())"], directory, 5, log)
            self.assertEqual(code, 0)
            self.assertIn(directory, log.read_text())

    def test_failure_preserves_exit_code_and_stderr(self):
        with tempfile.TemporaryDirectory() as directory:
            log = Path(directory) / "log"
            code = notifier.run_job([sys.executable, "-c", "import sys; print('falha', file=sys.stderr); sys.exit(7)"], directory, 5, log)
            self.assertEqual(code, 7)
            self.assertIn("falha", log.read_text())

    def test_timeout_stops_process(self):
        with tempfile.TemporaryDirectory() as directory:
            log = Path(directory) / "log"
            pidfile = Path(directory) / "pid"
            command = [sys.executable, "-c", f"import os,time; open({str(pidfile)!r},'w').write(str(os.getpid())); time.sleep(30)"]
            self.assertEqual(notifier.run_job(command, directory, 1, log), 124)
            pid = int(pidfile.read_text())
            with self.assertRaises(ProcessLookupError):
                os.kill(pid, 0)

    def test_command_not_found(self):
        with tempfile.TemporaryDirectory() as directory:
            self.assertEqual(notifier.run_job(["/nao-existe/comando"], directory, 5, Path(directory) / "log"), 127)

    def test_notification_failure_preserves_job_status_and_private_log(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch.dict(os.environ, {"TELEGRAM_BOT_TOKEN": FAKE_TOKEN, "TELEGRAM_CHAT_ID": "42"}, clear=True):
                with patch.object(notifier, "send_message", side_effect=notifier.NotificationError("sem rede")):
                    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                        code = notifier.main(["--log-dir", directory, "--run", sys.executable, "-c", "raise SystemExit(7)"])
            self.assertEqual(code, 7)
            log = next(Path(directory).glob("*.log"))
            self.assertEqual(log.stat().st_mode & 0o777, 0o600)

    def test_notification_does_not_include_command_arguments_or_log_contents(self):
        with tempfile.TemporaryDirectory() as directory:
            with patch.dict(os.environ, {"TELEGRAM_BOT_TOKEN": FAKE_TOKEN, "TELEGRAM_CHAT_ID": "42"}, clear=True):
                with patch.object(notifier, "send_message") as send, contextlib.redirect_stdout(io.StringIO()):
                    code = notifier.main(["--log-dir", directory, "--run", sys.executable, "-c", "print('DADO_PRIVADO')"])
            self.assertEqual(code, 0)
            self.assertNotIn("DADO_PRIVADO", send.call_args.args[2])
            self.assertNotIn("print(", send.call_args.args[2])


if __name__ == "__main__":
    unittest.main()
