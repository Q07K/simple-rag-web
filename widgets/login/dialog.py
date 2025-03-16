import streamlit as st


@st.dialog("Login Warning")
def login_page_dialog(text: str):
    st.write(text)
