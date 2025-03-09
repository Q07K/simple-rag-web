"""button_style module"""

import streamlit as st


def set_button() -> None:
    """streamlit button stlye 변경"""

    st.markdown(
        body="""<style>
        .st-emotion-cache-f6mfty {
        }
        .st-emotion-cache-f6mfty:hover {
            box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
            border: 1px solid rgba(49, 51, 63, 0.2) !important;
        }
        .st-emotion-cache-f6mfty:active {
            box-shadow: rgba(0, 0, 0, 0.06) 0px 2px 4px 0px inset;
            background-color: rgb(244, 241, 235);
            
        }
    </style>""",
        unsafe_allow_html=True,
    )
