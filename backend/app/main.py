from fastapi import FastAPI

app = FastAPI(
    title="IntentOS API",
    description="Backend API for IntentOS AI Desktop Agent",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to IntentOS 🚀",
        "status": "Backend is running successfully"
    }