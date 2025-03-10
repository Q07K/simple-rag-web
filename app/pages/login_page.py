import streamlit as st

from services.login_validator import email_validator, password_validator
from services.set_styles import set_styles

set_styles()

with st.form(key="login", border=False):
    _, col, _ = st.columns([0.2, 0.6, 0.2])

    col.title(body="Welcom")

    email = col.text_input(
        label="Email",
        placeholder="Enter email",
        key="email",
    )

    password = col.text_input(
        label="Password",
        placeholder="Enter password",
        type="password",
        key="password",
    )
    col.container(height=8, border=False)

    if col.form_submit_button(
        label="login",
        use_container_width=True,
    ):
        error_message = []
        if not email_validator(email=email):
            error_message.append("email")
        if not password_validator(password=password):
            error_message.append("password")

        if error_message:
            col.error(f"잘못된 ({" / ".join(error_message)}) 입니다.")
        else:
            st.switch_page(page="pages/chat_page.py")
