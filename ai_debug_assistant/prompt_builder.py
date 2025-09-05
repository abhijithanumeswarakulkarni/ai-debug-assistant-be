def build_prompt(error_log: str) -> str:
    return f"""
You are an expert software engineer.

Given the following error or stack trace:
{error_log}

Return ONLY valid JSON with this exact shape:
{{
  "explanation": "plain-English explanation of the root cause",
  "suggested_fix": "specific steps to fix or debug; include a small code snippet if helpful",
  "suggested_external_links": ["https://...", "https://...", "https://..."]
}}
No extra text.
""".strip()