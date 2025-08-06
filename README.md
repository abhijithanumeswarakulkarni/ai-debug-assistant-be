# AI Debug Assistant — Backend

FastAPI-powered backend for AI Debug Assistant — paste in an error message or stack trace, get a plain-English explanation, fix suggestions, and external resources using Groq's LLMs.

🔗 [Frontend Repo](https://github.com/abhijithanumeswarakulkarni/ai-debug-assistant-ui)

## 📦 Tech Stack

- **Backend**: FastAPI (Python)
- **LLM**: Groq (llama3-70b-8192)

## ✨ Features

- `/api/explain`: Accepts an error or stack trace and returns:
  - Explanation of the error
  - Suggested fix or debug steps
  - External reference links
- `/ping`: Health check endpoint

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

## 🚀 Getting Started

```bash
git clone https://github.com/abhijithanumeswarakulkarni/ai-debug-assistant-be.git
cd ai-debug-assistant-be
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

## 🧪 Example

# Request:

```
http POST /api/explain
{
  "error_log": "TypeError: 'int' object is not iterable"
}
```

# Response

```
{
  "explanation": "You're trying to iterate over an integer, which isn't iterable.",
  "suggested_fix": "Check where you're using a 'for' loop or comprehension and make sure the value is a list or iterable.",
  "suggested_external_links": [
    "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/is_not_iterable",
    "https://stackoverflow.com/questions/48242467/int-object-is-not-iterable-python-error",
    "https://bobbyhadz.com/blog/python-typeerror-int-object-is-not-iterable"
  ]
}
```
