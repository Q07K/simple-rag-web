import streamlit as st

from schemas.message_response import MessageModel
from services.set_styles import set_styles
from widgets.chats import first_chat_widget

if not st.session_state.get("is_loggedin", default=False):
    st.switch_page("pages/login_page.py")

# Set styles
set_styles()

# Main page
if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.messages:
    if user_query := first_chat_widget.first_chat():
        st.session_state.messages.append(
            MessageModel(
                role="user",
                content=user_query,
            )
        )
        st.session_state.messages.append(
            MessageModel(
                role="assistant",
                content="hi",
            )
        )
        st.rerun()
else:
    for message in st.session_state.messages:
        message: MessageModel
        with st.chat_message(name=message.role):
            st.markdown(body=message.content)

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
            st.markdown(body="hi")
        st.session_state.messages.append(
            MessageModel(
                role="assistant",
                content="hi",
            )
        )
