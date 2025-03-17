from pydantic import BaseModel


class ChatModel(BaseModel):
    id: str
    name: str


class ChatsModel(BaseModel):
    chats: list[ChatModel] | list[None]


class ChatsResponse(BaseModel):
    status: int
    message: str
    data: ChatsModel | None = None
