from pydantic import BaseModel

from schemas.message_response import MessagesModel


class ChatInitiateRequest(BaseModel):
    temperature: float
    max_tokens: int
    query: str


class ChatRequest(ChatInitiateRequest, MessagesModel): ...
