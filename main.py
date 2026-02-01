from fastapi import FastAPI
from pydantic import BaseModel
import os
import requests

app = FastAPI()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    if not GROQ_API_KEY:
        return {"error": "GROQ_API_KEY não encontrada"}

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "Você é um assistente útil."},
            {"role": "user", "content": req.message}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=20)
        response.raise_for_status()
        data = response.json()
        return {"reply": data["choices"][0]["message"]["content"]}
    except Exception as e:
        return {
            "error": "Falha ao chamar Groq",
            "details": str(e),
            "raw": response.text if 'response' in locals() else None
        }