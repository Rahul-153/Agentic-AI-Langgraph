from pydantic import BaseModel
from typing import List
from fastapi import FastAPI
from ai_agent import response_from_agent
import uvicorn

class requestState(BaseModel):
    """
    Represents the state of a request.
    """
    system_prompt: str
    messages: List[str]
    allow_search : bool
    model : str

ALLOWED_MODELS = ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "deepseek-r1-distill-llama-70b"]

app = FastAPI(title="LangGraph Agent")
@app.post("/chat")
def chat_endpoint(request : requestState):
    """
    Endpoint to handle chat requests.
    """
    if request.model not in ALLOWED_MODELS:
        return {"error": "Invalid model specified. Allowed models are: " + ", ".join(ALLOWED_MODELS)}
    
    response=response_from_agent(
        query=request.messages,
        system_prompt=request.system_prompt,
        model=request.model,
        allow_search=request.allow_search
    )
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")