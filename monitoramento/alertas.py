import os
import smtplib
from email.message import EmailMessage
from pathlib import Path
from dotenv import load_dotenv

# Localiza o arquivo .env na raiz do projeto
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")


def enviar_alerta(etapa, erro, run_id=None):
    remetente = os.getenv("GMAIL_REMETENTE")
    destinatario = os.getenv("GMAIL_DESTINATARIO")
    senha_app = os.getenv("GMAIL_SENHA_APP")

    if not all([remetente, destinatario, senha_app]):
        raise ValueError("Configurações do Gmail incompletas no arquivo .env")

    mensagem = EmailMessage()
    mensagem["From"] = remetente
    mensagem["To"] = destinatario
    mensagem["Subject"] = f"[ALERTA TECH CHALLENGE] Falha em {etapa}"

    mensagem.set_content(
        f"Foi identificada uma falha no pipeline.\n\n"
        f"Etapa: {etapa}\n"
        f"Run ID: {run_id}\n"
        f"Erro: {erro}\n\n"
        f"Verifique o arquivo execution_log.csv."
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=20) as servidor:
        servidor.login(remetente, senha_app.replace(" ", ""))
        servidor.send_message(mensagem)

    print(f"[ALERTA ENVIADO] Falha na etapa {etapa}")