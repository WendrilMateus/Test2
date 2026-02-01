import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

class ChatInput(BaseModel):
    message: str

    @app.get("/")
    def home():
        return {"status": "IA online"}

        @app.post("/chat")
        def chat(data: ChatInput):
            headers = {
                    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                            "Content-Type": "application/json"
                                }

                                    payload = {
                                            "model": "mistralai/mistral-7b-instruct",
                                                    "messages": [
                                                                {"role": "system", "content": "Você é uma IA criativa focada em criação de histórias e pesquisa."},
                                                                            {"role": "user", "content": data.message}
                                                                                    ]
                                                                                        }

                                                                                            response = requests.post(
                                                                                                    "https://openrouter.ai/api/v1/chat/completions",
                                                                                                            headers=headers,
                                                                                                                    json=payload
                                                                                                                        )

                                                                                                                            result = response.json()
                                                                                                                                answer = result["choices"][0]["message"]["content"]

                                                                                                                                    return {"response": answer}