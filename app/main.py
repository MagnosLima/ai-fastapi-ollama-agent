from fastapi import FastAPI
from app.schemas.chat import ChatRequest, ChatResponse
from app.agent.agent import agent_instance

app = FastAPI()


@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    response = await agent_instance.run(req.message)
    return ChatResponse(response=response)
