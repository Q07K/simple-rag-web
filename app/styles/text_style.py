"""button_style module"""

import streamlit as st


def set_title():
    """streamlit title stlye 변경"""

    st.markdown(
        body="""<style>
        h1 {
            text-align: center;
        }
    </style>""",
        unsafe_allow_html=True,
    )
