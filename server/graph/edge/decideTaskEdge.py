from typing import Literal
from models.pydantic.chatModel import ChatState
from langgraph.graph import END

def decide_task_edge(state: ChatState):
    if state.task != "chat":
        return END
    else:
        return state.task