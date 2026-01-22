from fastapi import APIRouter, HTTPException
from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_services import ChatService

router = APIRouter( tags=["chat"])

chat_service = ChatService()


@router.post("/chat", response_model=ChatResponse)
def chat_endpoint(payload: ChatRequest):
    print("Incoming payload:", payload)

    try:
        response = chat_service.generate_response(
            user_message=payload.message,
            chat_history=[]
        )
        print("LLM response:", response)
        return ChatResponse(response=response)

    except Exception as e:
        print("ERROR:", repr(e))  # 👈 THIS IS KEY
        raise HTTPException(status_code=500, detail=str(e))
