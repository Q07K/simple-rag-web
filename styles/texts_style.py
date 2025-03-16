"""texts style"""

import streamlit as st


def set_title_style():
    """set streamlit h1(title) style"""

    style = """
    <style>
        h1 {
            text-align: center;
        }
    </style>
    """
    st.markdown(body=style, unsafe_allow_html=True)
