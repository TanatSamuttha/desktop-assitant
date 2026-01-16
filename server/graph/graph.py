from langgraph.graph import StateGraph,START,END

from models.pydantic.chatModel import ChatState
from graph.nodes.chatNode import chat_node

builder = StateGraph(ChatState)
builder.add_node("chat", chat_node)
builder.add_node("search", )
builder.add_edge(START, "chat")
builder.add_edge("chat", "spliter")
builder.add_edge("spliter", END)

graph = builder.compile()