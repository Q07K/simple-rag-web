"""app module"""

from app.services.style_service import set_styles


def run() -> None:
    """run app"""
    # set styles
    set_styles()
