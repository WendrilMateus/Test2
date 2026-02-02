import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    url = "https://api.openai.com/v1/responses"

    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "gpt-4.1-mini",
        "input": req.message
    }

    response = requests.post(url, headers=headers, json=payload)

    # 👇 se a OpenAI devolver erro, mostramos
    if response.status_code != 200:
        return {
            "error": "Erro ao chamar OpenAI",
            "status_code": response.status_code,
            "details": response.text
        }

    data = response.json()

    reply = data.get("output_text")

    if not reply:
        return {
            "error": "Resposta inesperada da OpenAI",
            "raw_response": data
        }

    return {"reply": reply}