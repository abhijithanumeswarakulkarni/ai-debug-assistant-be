def build_prompt(error_log: str) -> str:
    return f"""
You are an expert software engineer. Given the following error or stack trace:

{error_log}

Respond strictly in raw JSON format with the following structure:
{{
  "explanation": "<plain-English explanation of the error>",
  "suggested_fix": "<suggestion to fix or debug with optional code snippet if neccessary>",
  "suggested_external_links": "<scrape through web and pick top 3 links matching the error message>"
}}

Do not include any commentary, markdown, or formatting outside of the JSON block.
""".strip()
