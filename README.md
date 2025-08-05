# ai-debug-assistant

Paste in an error message or stack trace, get a clear explanation and fix suggestion from an AI.

## 🔧 Tech Stack
- **Backend**: FastAPI (Python)
- **LLM**: Groq llama3-70b-8192
- **Frontend**: Svelte

## 🚀 Features
- `/api/explain`: Accepts an error message or stack trace and returns:
  - A plain-English explanation
  - Suggested code fix or debugging steps
- `/ping` : Health check

## 📂 Project Structure
```
ai_debug_assistant/
├── main.py               # FastAPI app and route setup
├── prompt_builder.py     # Prompt construction logic for LLM
├── groq_client.py        # Environment and Groq key config
├── schemas.py
├── __init__.py
.gitignore
.env                      # Stores Groq API key
requirements.txt          # Dependencies
README.md
```

## ▶️ Quickstart
1. **Clone the repo**
```bash
git clone https://github.com/abhijithanumeswarakulkarni/ai-debug-assistant-be.git
cd ai-debug-assistant-be
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set environment variables**
Create a `.env` file with:
```
GROQ_API_KEY=<your-api-key>
GROQ_MODEL=<model-you-want-to-use> ex: llama3-70b-8192
```

4. **Run the FastAPI server**
```bash
uvicorn ai_debug_assistant.main:app --reload
```

5. **Test the API**
POST to `http://localhost:8000/api/explain` with JSON:
```json
{
  "error_log": "TypeError: 'int' object is not iterable"
}

**Response**:
{
  "explanation": "You're trying to iterate over an integer, which isn't iterable.",
  "suggested_fix": "Check where you're using a 'for' loop or comprehension and make sure the value is a list or iterable."
}
```
