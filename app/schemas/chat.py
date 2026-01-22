from pydantic import BaseModel, Field
from typing import Optional


class ChatRequest(BaseModel):
    """
    Incoming chat request from client.

    """
    session_id: str = Field(
        description="Unique session ID for the conversation",
        example="session_123"   # ✅ singular `example`
    )
    message: str = Field(
        description="User message",
        example="Explain transformers simply"
    )



class ChatResponse(BaseModel):
    """
    Chat response returned to the client.
    """

    response: str = Field(
        description="LLM generated response",
        example="Transformers are neural networks that use attention..."
    )