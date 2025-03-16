import streamlit as st

from apis.chats_api import get_messages_by_chat_id
from schemas.chat_response import ChatModel


def chat_session_block(model: ChatModel):
    left_field, right_field = st.columns([0.8, 0.2])

    with left_field.container():
        st.button(
            label=model.name,
            key=f"title_{model.id}",
            use_container_width=True,
            on_click=get_messages_by_chat_id,
            args=model.id,
        )

    with right_field.container():
        st.button(
            label="🗑️",
            key=f"delete_{model.id}",
            use_container_width=True,
        )
