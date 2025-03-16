import streamlit as st

from services.set_styles import set_styles

if not st.session_state.get("is_loggedin", default=False):
    st.switch_page("pages/login_page.py")


set_styles()

st.text("hi")
