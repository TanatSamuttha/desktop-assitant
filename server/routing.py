from fastapi import FastAPI

app = FastAPI()

@app.get("/test")
async def TestEndpoint():
    return {"result": "success"}