

from ai_agent_llm import init_action
from pydantic import BaseModel
from fastapi import FastAPI

class Query(BaseModel):
    query: str


app = FastAPI(title="AI Agent App")
@app.post("/answer")
async def answer(query : Query):

    response = init_action(query)
    return {"Answer": response}

