from fastapi import APIRouter
from app.models.schemas import ChatRequest, ChatResponse
from app.services.chat_services import chat

router =APIRouter()

@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(request:ChatRequest):
    answer = chat(
        session_id=request.session_id,
        domain=request.domain,
        user_input=request.message
    
    )
    return ChatResponse(response=answer)