from fastapi import FastAPI
from model.LLM import llm

app = FastAPI()

@app.post("/message")
async def TestEndpoint():
    return {"result": "success"}