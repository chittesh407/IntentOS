from fastapi import APIRouter
from pydantic import BaseModel

from app.llm.provider import generate_response
from app.planner.planner import Planner, IntentType
from app.executor.executor import Executor

router = APIRouter()

planner = Planner()

executor = Executor()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
async def chat(request: ChatRequest):

    prompt = request.message

    intent = planner.classify(prompt)

    if intent == IntentType.CHAT:
        reply = generate_response(prompt)

        return {
            "intent": intent.value,
            "response": reply
        }

    elif intent == IntentType.EXECUTE:
        result = executor.execute(prompt)

        return {
            "intent": intent.value,
            "response": result
        }

    elif intent == IntentType.SYSTEM:
        return {
            "intent": intent.value,
            "response": "💻 System Information module coming next."
        }

    elif intent == IntentType.FILE:
        return {
            "intent": intent.value,
            "response": "📁 File Search module coming next."
        }

    return {
        "intent": "unknown",
        "response": "I couldn't classify the request."
    }