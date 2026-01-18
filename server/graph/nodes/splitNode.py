from models.pydantic.chatModel import ChatState

async def split_node(state: ChatState) -> ChatState:
    voice_response, text_response, task, url = state.raw_response.split("-<([split])>-")
    return {
        "user_message": state.user_message,
        "voice_response": voice_response,
        "text_response": text_response,
        "task": task,
        "url": url
    }