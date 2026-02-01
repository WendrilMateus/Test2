import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel

# ======================
# Inicialização do app
# ======================
app = FastAPI()

# ======================
# Variável de ambiente
# ======================
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ======================
# Modelo de entrada
# ======================
class ChatRequest(BaseModel):
    message: str

# ======================
# Rota raiz (teste)
# ======================
@app.get("/")
def root():
    return {"status": "ok"}

# ======================
# Rota de chat com IA
# ======================
@app.post("/chat")
def chat(req: ChatRequest):
    if not GROQ_API_KEY:
        return {"error": "GROQ_API_KEY não configurada"}

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        # MODELO ATIVO (não aposentado)
        "model": "llama3-70b-8192",
        "messages": [
            {
                "role": "system",
                "content": "Você é um assistente criativo, claro e útil."
            },
            {
                "role": "user",
                "content": req.message
            }
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=30
        )

        response.raise_for_status()
        data = response.json()

        return {
            "reply": data["choices"][0]["message"]["content"]
        }

    except requests.exceptions.RequestException as e:
        return {
            "error": "Erro ao chamar a Groq",
            "details": str(e),
            "status_code": getattr(e.response, "status_code", None),
            "response": getattr(e.response, "text", None)
        }