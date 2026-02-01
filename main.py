from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"ok": True}

@app.post("/chat")
def chat(data: ChatRequest):
    return {"reply": data.message}