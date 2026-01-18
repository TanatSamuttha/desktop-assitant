from models.pydantic.chatModel import ChatState

async def split_node(state: ChatState) -> ChatState:
    task, url = state.raw_response.split("-<([split])>-")
    return {
        "user_message": state.user_message,
        "task": task,
        "url": url
    }