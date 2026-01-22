from pydantic import BaseModel, Field
from typing import Optional


class ChatRequest(BaseModel):
    """
    Incoming chat request from client.

    """
    session_id:str = Field(
        ...,
        description = "Unique session identifier for the chat converstation",
        examples="session_123"

    )
    message:str=Field(
        ...,
        description="User input message",
        example="Explain transformers in simple terms"
    )


class ChatResponse(BaseModel):
    """
    Chat response returned to the client.
    """
    session_id:str = Field(
        ...,
        description = "Unique session identifier for the chat converstation",
        examples="session_123"
    )
    answer:str=Field(
        ...,    
        description="LLM-generatred response message",
        examples="Transformers are neural networks that process text using attention..."
    )