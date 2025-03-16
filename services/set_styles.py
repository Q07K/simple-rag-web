"""styles setting module"""

from styles.button_style import set_button_style
from styles.chat_message_style import (
    disable_messagge_icon,
    set_user_message_style,
)
from styles.fonts_style import set_font
from styles.texts_style import set_title_style


def set_styles() -> None:
    """set streamlit styles"""
    set_font()
    set_button_style()
    set_user_message_style()
    disable_messagge_icon()
    set_title_style()
