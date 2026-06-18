import os 
import requests
import logging 
from dotenv import load_dotenv
from supabase import create_client


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")

def procurar_contatos():
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    response = supabase.table("contatos").select("*").limit(3).execute()
    logging.info(f"total de contatos encontrados: {len(response.data)}")
    return response.data

def enviar_mensagem(telefone, nome):
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"
    headers = {
        "Content-Type": "application/json",
        "Client-Token": ZAPI_CLIENT_TOKEN
    }
    payload = {
        "phone": telefone,
        "message": f"Olá, {nome} tudo bem com você?"
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        logging.info(f"mensagem enviada com sucesso para {nome}")
    else:
        logging.error(f"erro ao enviar mensagem para {nome}, status: {response.status_code}")


def main():
    logging.info("iniciando o envio de mensagens!!")
    contatos = procurar_contatos()

    if not contatos:
        logging.warning("nenhum contato encontrado.")
        return

    for contato in contatos:
        nome = contato.get("nome")
        telefone = contato.get("telefone")
        enviar_mensagem(telefone, nome)

    logging.info("envio de mensagem finalizado!!")


if __name__ == "__main__":
    main()