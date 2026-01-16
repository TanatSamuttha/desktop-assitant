from fastapi import FastAPI
from services.callLLM import CallLLM

app = FastAPI()

@app.post("/message")
async def TestEndpoint():
    return {"result": "success"}