from fastapi import FastAPI
from app.schemas.chat import ChatRequest, ChatResponse

app = FastAPI()

@app.post('/chat', response_model=ChatResponse)
def chat(req: ChatRequest):
    return ChatResponse(response=f"Echo: {req.message}")
