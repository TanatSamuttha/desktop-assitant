from fastapi import FastAPI
from services.callAssistant import callAssistant
from models.pydantic.requestModel import Request

app = FastAPI()

@app.post("/call-assistant")
async def TestEndpoint(req: Request):
    await callAssistant(req.user_message)
    return {"result": "success"}