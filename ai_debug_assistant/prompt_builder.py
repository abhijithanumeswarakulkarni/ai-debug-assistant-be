def build_prompt(error_log: str) -> str:
    return f"""
You're an expert software engineer helping a developer debug code.

Given this error or stack trace:

{error_log}

Respond with:
1. A plain-English explanation of what the error means
2. A suggestion to fix or debug it, including code if helpful
""".strip()
