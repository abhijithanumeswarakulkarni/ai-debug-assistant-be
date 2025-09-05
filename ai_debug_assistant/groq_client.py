# groq_client.py
import os, json, requests

BASE = "https://api.groq.com/openai/v1"
MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")  # current model

def get_groq_response(prompt: str) -> dict:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY missing")

    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt or "Hello"}],
        "max_tokens": 1000,                         # avoid truncation
        "temperature": 0,                           # deterministic JSON
        "response_format": {"type": "json_object"}  # force JSON output
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
        # Bubble up the provider's error body
        try:
            err = r.json()
        except Exception:
            err = {"text": r.text}
        raise RuntimeError(f"Groq {r.status_code}: {err}")

    text = r.json()["choices"][0]["message"]["content"]

    # Parse model text to a Python dict so API returns an object, not a string
    try:
        obj = json.loads(text)
        if not isinstance(obj, dict):
            raise ValueError("Response is not a JSON object")
        return obj
    except Exception:
        # Fallback to keep UI functional
        return {
            "explanation": text.strip(),
            "suggested_fix": "No structured fix provided.",
            "suggested_external_links": []
        }