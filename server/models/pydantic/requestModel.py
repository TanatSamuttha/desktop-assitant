from pydantic import BaseModel
from langchain.schema import BaseMessage
from typing import Optional

class Request(BaseModel):
    user_message: str