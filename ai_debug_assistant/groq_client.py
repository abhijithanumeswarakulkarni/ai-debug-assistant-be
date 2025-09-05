import os, requests

BASE = "https://api.groq.com/openai/v1"
MODEL = os.getenv("GROQ_MODEL", "llama-3.1-70b-versatile")

def get_groq_response(prompt: str) -> str:
    api_key = os.getenv("GROQ_API_KEY")
    assert api_key, "GROQ_API_KEY missing"

    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt or "Hello"}],
        "max_tokens": 256
    }

    r = requests.post(
        f"{BASE}/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        json=payload,
        timeout=30,
    )

    if not r.ok:
        # show Groq's actual complaint
        try:
            print("Groq error body:", r.json())
        except Exception:
            print("Groq error text:", r.text)
        r.raise_for_status()

    return r.json()["choices"][0]["message"]["content"]