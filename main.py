from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatInput(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "IA online"}

@app.post("/chat")
def chat(data: ChatInput):
    user_message = data.message
    resposta = f"Você disse: {user_message}"
    return {"response": resposta}