from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_services import ChatService

router = APIRouter(tags=["chat"])

chat_service = ChatService()


@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(payload: ChatRequest):
    try:
        response = chat_service.generate_response(
            session_id=payload.session_id,
            user_message=payload.message
        )
        return ChatResponse(response=response)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating LLM response: {str(e)}"
        )
