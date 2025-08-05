import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_groq_response(prompt: str) -> str:
    api_key = os.getenv("GROQ_API_KEY")
    model = os.getenv("GROQ_MODEL", "llama3-70b-8192")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    res = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
    res.raise_for_status()
    return res.json()["choices"][0]["message"]["content"]