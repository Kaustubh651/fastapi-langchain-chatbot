from fastapi import FastAPI
from app.api.chat import router as chat_router

app = FastAPI(
        title="Chatbot API",
        description="Production-ready chatbot API using FastAPI, LangChain, and Hugging Face",
        version="1.0.0"
    )

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(chat_router,prefix="/api/v1", tags=["chat"]  )