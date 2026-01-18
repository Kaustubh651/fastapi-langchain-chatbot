from pydantic import BaseModel

class ChatRequest(BaseModel):
    session_id: str
    message: str
    domain: str = "AI"

class ChatResponse(BaseModel):
    response: str
