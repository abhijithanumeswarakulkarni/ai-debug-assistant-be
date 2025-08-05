from pydantic import BaseModel

class ErrorRequest(BaseModel):
    error_log: str