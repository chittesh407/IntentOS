from fastapi import FastAPI
from app.api.chat import router as chat_router

app = FastAPI(
    title="IntentOS API"
)

app.include_router(chat_router)

@app.get("/")
def home():
    return {
        "message":"IntentOS Backend Running 🚀"
    }