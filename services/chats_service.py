import streamlit as st

from apis import chats_api
from apis.chats_api import get_messages_by_chat_id
from schemas.chat_response import ChatModel


def get_messages(chat_id: str):
    response = get_messages_by_chat_id(chat_id=chat_id)
    if response:
        models = response.data.messages
        st.session_state.messages = models


@st.dialog("Delete Chat")
def delete_chat(model: ChatModel):
    st.markdown(f"""### Title:\n\n`{model.name}`을 정말 삭제하시겠습니까?""")
    _, left_field, _, right_field, _ = st.columns([0.1, 0.3, 0.1, 0.3, 0.1])
    delete_no = left_field.button("No", use_container_width=True)
    delete_yes = right_field.button("Yes", use_container_width=True)
    if delete_yes:
        with st.spinner("처리중..."):
            chats_api.delete_chat_by_chat_id(chat_id=model.id)
        st.rerun()

    if delete_no:
        st.rerun()
