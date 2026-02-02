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

    data = response.json()

    reply = data["output"][0]["content"][0]["text"]

    return {"reply": reply}