from fastapi import FastAPI
from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

app = FastAPI()

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    # For now, just return example response
    return ChatResponse(response=f"Echo: {req.message}")

