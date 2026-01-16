from fastapi import FastAPI
from model.LLM import llm

app = FastAPI()

@app.get("/test")
async def TestEndpoint():
    return {"result": "success"}