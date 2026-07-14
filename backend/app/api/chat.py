from fastapi import APIRouter
from pydantic import BaseModel

from app.agent.agent import Agent

router = APIRouter()

agent = Agent()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
async def chat(request: ChatRequest):

    response = agent.handle(request.message)

    return response