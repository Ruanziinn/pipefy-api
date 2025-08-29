import os
from dotenv import load_dotenv

load_dotenv()

PIPEFY_TOKEN = os.getenv("PIPEFY_API_TOKEN")
if not PIPEFY_TOKEN:
    raise ValueError("A variável de ambiente PIPEFY_API_TOKEN não foi encontrada.")

PIPE_ID = os.getenv("PIPE_ID")
if not PIPE_ID:
    raise ValueError("A variável de ambiente PIPE_ID não foi encontrada.")

PIPEFY_URL = "https://api.pipefy.com/graphql"

CIDADES = {
    "Caucaia": "850256822",
    "Maranguape": "850256601",
    "Fortaleza": "850256930",
    "Maracanaú": "850256388",
    "Eusébio": "850256710"
}

FASE_FINAL_ID = "323403004"

headers = {
    'Authorization': f'Bearer {PIPEFY_TOKEN}',
    'Content-Type': 'application/json'
}