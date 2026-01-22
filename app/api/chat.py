from http.client import HTTPException
from fastapi import APIRouter,HTTPException, status

from app.models.schemas import ChatRequest, ChatResponse
from app.services.chat_services import ChatService


router =APIRouter()
chat_service = ChatService()    


@router.post(
        "/chat", 
        response_model=ChatResponse
        status_code = status.HTTP_200_OK
    )

# ---------------- Sprint 1: Basic LLM Chat Service Endpoint Implementation

# def chat_endpoint(request:ChatRequest):
#     answer = chat(
#         session_id=request.session_id,
#         domain=request.domain,
#         user_input=request.message
    
#     )
#     return ChatResponse(response=answer)

#------------------------------------------ SPRINT-2 : Using Dynamic Prompts with Langchain---------------
def chat_endpoint(request:ChatRequest):
    """
    chat endpoint to interact with LLM using dynamic prompts.
    """

    try: 
        answer = chat_service.generate_response(
            user_message = request.message,
            chat_history=[]
        )

        return ChatResponse(
            session_id = request.session_id,
            answer = answer
        )
    except RuntimeError as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

