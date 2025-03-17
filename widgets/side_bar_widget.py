import streamlit as st

from apis import chats_api
from services.chats_service import delete_session_state_messages
from widgets.chats.chat_session_widget import chat_session_block


def sidebar():
    with st.sidebar:
        st.header("모델 설정")
        st.slider(
            label="temperature",
            key="temperature",
            min_value=0.0,
            max_value=1.0,
            value=0.5,
        )
        st.slider(
            label="max_tokens",
            key="max_tokens",
            min_value=0,
            max_value=1000,
            value=100,
        )
        st.header(" 대화")
        st.button(
            "새로운 대화",
            use_container_width=True,
            icon="➕",
            on_click=delete_session_state_messages,
        )
        response = chats_api.get_chats()
        if response:
            models = response.data.chats[::-1]
            for model in models:
                chat_session_block(model=model)
