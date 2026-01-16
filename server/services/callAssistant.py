from graph.graph import graph

async def callAssistant(user_message: str):
    print(user_message)
    finalState = await graph.ainvoke({"user_message": user_message})