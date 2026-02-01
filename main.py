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

    response = requests.post(url, headers=headers, json=payload)

    data = response.json()
    reply = data["choices"][0]["message"]["content"]

    return {"reply": reply}