"""button_style module"""

import streamlit as st


def set_user_message_field() -> None:
    """streamlit chat_message("user") stlye 변경"""

    st.markdown(
        body="""<style>
        .st-emotion-cache-1c7y2kd {
            flex-direction: row-reverse;
            border-radius: 25px;
            background-color: #F0EBE3;
            padding: 8px 16px;
            width: fit-content;
            max-width: 100%;
            margin-left: auto;
        }
    </style>""",
        unsafe_allow_html=True,
    )


def disable_messagge_icon() -> None:
    """streamlit chat_message("user") icon 제거"""

    st.markdown(
        body="""<style>
        .st-emotion-cache-1ghhuty, .st-emotion-cache-bho8sy {
        display: none;
        }
        </style>""",
        unsafe_allow_html=True,
    )
