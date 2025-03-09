"""button_style module"""

import streamlit as st


def set_font():
    """streamlit font 변경"""

    st.markdown(
        body="""<style>
        @font-face {
            font-family: 'Pretendard-Regular';
            src: url('https://fastly.jsdelivr.net/gh/Project-Noonnu/noonfonts_2107@1.1/Pretendard-Regular.woff') format('woff');
            font-weight: 400;
            font-style: normal;
        }
        html, body, div, p, h1, h2, h3, [class*="css"] {
            font-family: 'Pretendard-Regular', sans-serif !important;
            color: #212121;
        }
    </style>""",
        unsafe_allow_html=True,
    )
