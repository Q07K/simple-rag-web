import streamlit as st

from apis.chats_api import generate, generate_initiate
from schemas.chat_stream import ChatStream
from schemas.message_response import MessageModel


def stream_generate_initiate(
    temperature: float,
    max_tokens: int,
    query: str,
):
    chunk = ""
    response: ChatStream
    for response in generate_initiate(
        temperature=temperature,
        max_tokens=max_tokens,
        query=query,
    ):
        if response.message == "create message successful":
            st.session_state.chat_id = response.data.chat_id
            st.session_state.messages.append(
                MessageModel(
                    role="assistant",
                    content=chunk,
                )
            )
        else:
            chunk += response.message
            yield response.message


def stream_generate(
    temperature: float,
    max_tokens: int,
    messages: list[MessageModel],
    query: str,
    chat_id: str,
):
    chunk = ""
    response: ChatStream
    for response in generate(
        temperature=temperature,
        max_tokens=max_tokens,
        messages=messages,
        query=query,
        chat_id=chat_id,
    ):
        chunk += response.message
        yield response.message

    st.session_state.messages.append(
        MessageModel(
            role="assistant",
            content=chunk,
        )
    )
