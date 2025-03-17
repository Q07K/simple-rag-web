from pydantic import BaseModel


class MessageModel(BaseModel):
    role: str
    content: str


class MessagesModel(BaseModel):
    messages: list[MessageModel] | list[None]


class MessagesResponse(BaseModel):
    status: int
    message: str
    data: MessagesModel | None = None
