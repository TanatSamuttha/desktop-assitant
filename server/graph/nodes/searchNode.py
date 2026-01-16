import webbrowser
from models.pydantic.chatModel import ChatState

async def search_node(state: ChatState) -> ChatState:
    url = state.url
    print(url)
    webbrowser.open(url)
    return state