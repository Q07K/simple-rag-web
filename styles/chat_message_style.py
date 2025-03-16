"""chat message style"""

import streamlit as st


def set_user_message_style():
    """set streamlit user message style"""

    style = """
    <style>
        .st-emotion-cache-1c7y2kd {
            flex-direction: row-reverse;
            border-radius: 25px;
            background-color: #F0EBE3;
            padding: 8px 16px;
            width: fit-content;
            max-width: 100%;
            margin-left: auto;
        }
    </style>
    """
    st.markdown(body=style, unsafe_allow_html=True)


def disable_messagge_icon():
    """set streamlit message icon disable"""

    style = """
    <style>
        .st-emotion-cache-1ghhuty, .st-emotion-cache-bho8sy {
            display: none;
        }
    </style>
    """
    st.markdown(body=style, unsafe_allow_html=True)
