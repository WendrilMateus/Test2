import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

class ChatInput(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "IA online"}

@app.post("/chat")
def chat(data: ChatInput):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {
                "role": "system",
                "content": "Você é uma IA criativa focada em criação de histórias e pesquisa."
            },
            {
                "role": "user",
                "content": data.message
            }
        ]
    }

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers=headers,
        json=payload
    )

    result = response.json()
    answer = result["choices"][0]["message"]["content"]

    return {"response": answer}