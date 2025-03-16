import streamlit as st

from apis import chats_api
from widgets.chats.chat_session_widget import chat_session_block


def sidebar():
    with st.sidebar:
        response = chats_api.get_chats()
        if response:
            models = response.data.chats
            for model in models:
                chat_session_block(model=model)
