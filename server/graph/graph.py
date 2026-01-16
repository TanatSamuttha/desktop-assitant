from langgraph.graph import StateGraph,START,END

from models.pydantic.chatModel import ChatState
from graph.nodes.chatNode import chat_node
from graph.nodes.searchNode import search_node
from graph.nodes.splitNode import split_node

builder = StateGraph(ChatState)
builder.add_node("chat", chat_node)
builder.add_node("search", search_node)
builder.add_node("split", split_node)
builder.add_edge(START, "chat")
builder.add_edge("chat", "search")
builder.add_edge("search", "split")
builder.add_edge("split", END)

graph = builder.compile()