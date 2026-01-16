from pydantic import BaseModel
from langchain.schema import BaseMessage
from typing import Optional

class ChatState(BaseModel):
    user_message: str
    task: str
    link: str