import streamlit as st

from schemas.message_response import MessageModel
from services.chat_stream_service import (
    stream_generate,
    stream_generate_initiate,
)
from services.set_styles import set_styles
from widgets.chats import first_chat_widget
from widgets.side_bar_widget import sidebar

if not st.session_state.get("is_loggedin", default=False):
    st.switch_page("pages/login_page.py")

# Set styles
set_styles()

# Set Side Bar
sidebar()

# Main page
if "messages" not in st.session_state:
    st.session_state.messages = []
if "temperature" not in st.session_state:
    st.session_state.temperature = 0.5
if "max_tokens" not in st.session_state:
    st.session_state.max_tokens = 100

if not st.session_state.messages:
    if user_query := first_chat_widget.first_chat():
        st.session_state.messages.append(
            MessageModel(
                role="user",
                content=user_query,
            )
        )
        st.rerun()
else:
    for message in st.session_state.messages:
        message: MessageModel
        with st.chat_message(name=message.role):
            st.markdown(body=message.content)

    # 첫 대화
    if len(st.session_state.messages) == 1:
        with st.chat_message(name="ai"):
            with st.spinner():
                stream = stream_generate_initiate(
                    temperature=st.session_state.temperature,
                    max_tokens=st.session_state.max_tokens,
                    query=st.session_state.messages[0].content,
                )
                next(stream)
            st.write_stream(stream=stream)
        st.rerun()

    if user_query := st.chat_input():
        with st.chat_message(name="user"):
            st.markdown(body=user_query)
        st.session_state.messages.append(
            MessageModel(
                role="user",
                content=user_query,
            )
        )

        with st.chat_message(name="ai"):
            with st.spinner():
                stream = stream_generate(
                    temperature=st.session_state.temperature,
                    max_tokens=st.session_state.max_tokens,
                    messages=st.session_state.messages[:-1],
                    query=user_query,
                    chat_id=st.session_state.chat_id,
                )
                next(stream)
            st.write_stream(stream=stream)
        st.rerun()
