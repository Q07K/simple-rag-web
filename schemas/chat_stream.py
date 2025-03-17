from pydantic import BaseModel


class ChatData(BaseModel):
    chat_id: str


class ChatStream(BaseModel):
    status: int = 200
    message: str
    data: None | ChatData = None
