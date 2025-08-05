from ai_debug_assistant.schemas import ErrorRequest
from fastapi import FastAPI, HTTPException
from ai_debug_assistant.prompt_builder import build_prompt
from ai_debug_assistant.groq_client import get_groq_response

app = FastAPI()

@app.post("/api/explain")
async def explain(payload: ErrorRequest):
    try:
        print("Received error log:", payload.error_log)
        prompt = build_prompt(payload.error_log)
        result = get_groq_response(prompt)
        print("Groq Request Successful")
        return {"response": result}
    except Exception as e:
        print("Groq Request Failed:", e)
        raise HTTPException(status_code=500, detail=str(e))