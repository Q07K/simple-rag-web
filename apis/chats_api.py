from apis import api_url
from apis.api_wrapper import ApiWrapper
from schemas.chat_response import ChatsResponse
from schemas.message_response import MessagesResponse


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
