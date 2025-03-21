from apis import api_url
from apis.api_wrapper import ApiWrapper
from schemas.chat_request import ChatInitiateRequest, ChatRequest
from schemas.chat_response import ChatsResponse
from schemas.chat_stream import ChatStream
from schemas.message_response import MessageModel, MessagesResponse


def get_chats() -> ChatsResponse | None:
    return ApiWrapper().get(url=api_url.CHATS, schema=ChatsResponse)


def get_messages_by_chat_id(chat_id: str) -> MessagesResponse | None:
    return ApiWrapper().get(
        url=api_url.CHATS + f"/{chat_id}",
        schema=MessagesResponse,
    )


def delete_chat_by_chat_id(chat_id: str) -> ChatsResponse | None:
    return ApiWrapper().delete(
        url=api_url.CHATS + f"/{chat_id}",
        schema=ChatsResponse,
    )


def generate_initiate(temperature: float, max_tokens: int, query: str):
    return ApiWrapper().stream(
        url=api_url.CHATS + "/initiate",
        data=ChatInitiateRequest(
            temperature=temperature,
            max_tokens=max_tokens,
            query=query,
        ).model_dump_json(),
        schema=ChatStream,
    )


def generate(
    temperature: float,
    max_tokens: int,
    query: str,
    chat_id: str,
    messages: list[MessageModel],
):
    return ApiWrapper().stream(
        url=api_url.CHATS + f"/{chat_id}/generate",
        data=ChatRequest(
            temperature=temperature,
            max_tokens=max_tokens,
            query=query,
            messages=messages,
        ).model_dump_json(),
        schema=ChatStream,
    )
