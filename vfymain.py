
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="My Agent")

class AgentRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "online", "name": "My Agent"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/agent")
def run_agent(request: AgentRequest):
    return {
        "status": "success",
        "response": f"Agent received: {request.message}"
    }

