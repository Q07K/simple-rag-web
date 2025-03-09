"""style_service module"""

from app.styles import button_style, chat_style, font_style, text_style


def set_styles() -> None:
    """Streamlit 디자인 설정"""
    font_style.set_font()
    text_style.set_title()
    chat_style.set_user_message_field()
    chat_style.disable_messagge_icon()
    button_style.set_button()
