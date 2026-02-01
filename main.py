import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel

@app.post("/chat")
def chat(data: ChatInput):
    if not GROQ_API_KEY:
            return {
                        "error": "GROQ_API_KEY não configurada"
                                }

                                    headers = {
                                            "Authorization": f"Bearer {GROQ_API_KEY}",
                                                    "Content-Type": "application/json"
                                                        }

                                                            payload = {
                                                                    "model": "llama3-8b-8192",
                                                                            "messages": [
                                                                                        {
                                                                                                        "role": "system",
                                                                                                                        "content": "Você é uma IA criativa focada em criação de histórias."
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

                                                                                                                                                                                                                                            if response.status_code != 200:
                                                                                                                                                                                                                                                    return {
                                                                                                                                                                                                                                                                "error": "Erro ao chamar Groq",
                                                                                                                                                                                                                                                                            "status_code": response.status_code,
                                                                                                                                                                                                                                                                                        "details": response.text
                                                                                                                                                                                                                                                                                                }

                                                                                                                                                                                                                                                                                                    result = response.json()

                                                                                                                                                                                                                                                                                                        if "choices" not in result:
                                                                                                                                                                                                                                                                                                                return {
                                                                                                                                                                                                                                                                                                                            "error": "Resposta inesperada do Groq",
                                                                                                                                                                                                                                                                                                                                        "details": result
                                                                                                                                                                                                                                                                                                                                                }

                                                                                                                                                                                                                                                                                                                                                    return {
                                                                                                                                                                                                                                                                                                                                                            "response": result["choices"][0]["message"]["content"]
                                                                                                                                                                                                                                                                                                                                                                }