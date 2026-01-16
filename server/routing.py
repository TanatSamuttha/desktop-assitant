from fastapi import FastAPI
from services.callAssistant import callAssistant

app = FastAPI()

@app.post("/call-assistant")
async def TestEndpoint():
    return {"result": "success"}