from fastapi import APIRouter

router = APIRouter()

@router.post("/chat")
async def chat(message: dict):
    return {
        "response": "Backend Connected 🚀",
        "received": message
    }