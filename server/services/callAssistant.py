from graph.graph import graph

async def callAssistant(user_message: str):
    finalState = graph.invoke({"user_message": user_message})