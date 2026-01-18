from pydantic import BaseModel
from typing import Optional

class ChatState(BaseModel):
    user_message: str
    raw_response: Optional[str] = None
    voice_response: Optional[str] = None
    text_response: Optional[str] = None
    task: Optional[str] = None
    url: Optional[str] = None