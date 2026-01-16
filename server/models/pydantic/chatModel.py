from pydantic import BaseModel
from typing import Optional

class ChatState(BaseModel):
    user_message: str
    raw_response: str
    task: Optional[str] = None
    link: Optional[str] = None