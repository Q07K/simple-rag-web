from pydantic import BaseModel


class ChatInitiateRequest(BaseModel):
    temperature: float
    max_tokens: int
    query: str
