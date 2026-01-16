from langchain.schema import AIMessage, HumanMessage
from models.pydantic.chatModel import ChatState
from models.llm.llm import llm, prompt

async def chat_node(state: ChatState) -> ChatState:
    messages = prompt.format_messages(
        user_input = state.user_message
    )

    response = await llm.ainvoke(messages)

    return {
        "user_message": state.user_message,
        "raw_response": response.text
    }