from models.pydantic.chatModel import ChatState

async def split_node(state: ChatState) -> ChatState:
    task, link = state.raw_response.split()
    return {
        "task": task,
        "link": link
    }