import streamlit as st

from apis import auth_api
from services.login_validator import email_validator, password_validator
from services.set_styles import set_styles
from widgets.login.dialog import login_page_dialog

set_styles()

with st.form(key="login", border=False):
    _, col, _ = st.columns([0.2, 0.6, 0.2])

    col.title(body="Welcome")

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
        if not email_validator(email=email):
            login_page_dialog("Email 형식을 다시 확인해주세요.")
        elif not password_validator(password=password):
            login_page_dialog("Password 형식을 다시 확인해주세요.")
        else:
            if auth_api.login(email=email, password=password):
                st.session_state["is_loggedin"] = True
                st.switch_page(page="pages/chat_page.py")
            else:
                login_page_dialog("(email / password)를 다시 확인해주세요.")
