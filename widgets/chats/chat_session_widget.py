import streamlit as st

from schemas.chat_response import ChatModel
from services.chats_service import delete_chat, get_messages


def chat_session_block(model: ChatModel):
    left_field, right_field = st.columns([0.8, 0.2])

    with left_field.container():
        st.button(
            label=model.name,
            key=f"title_{model.id}",
            use_container_width=True,
            on_click=get_messages,
            kwargs={"chat_id": model.id},
        )

    with right_field.container():
        st.button(
            label="🗑️",
            key=f"delete_{model.id}",
            use_container_width=True,
            on_click=delete_chat,
            kwargs={"model": model},
        )
