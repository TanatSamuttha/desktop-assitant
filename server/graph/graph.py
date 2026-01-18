from langgraph.graph import StateGraph,START,END

from models.pydantic.chatModel import ChatState
from graph.nodes.chatNode import chat_node
from graph.nodes.splitNode import split_node
from graph.nodes.searchNode import search_node
from graph.edge.decideTaskEdge import decide_task_edge

builder = StateGraph(ChatState)
builder.add_node("chat", chat_node)
builder.add_node("search", search_node)
builder.add_node("split", split_node)
builder.add_edge(START, "chat")
builder.add_edge("chat", "split")
builder.add_conditional_edges("split", decide_task_edge)
builder.add_edge("search", END)

graph = builder.compile()