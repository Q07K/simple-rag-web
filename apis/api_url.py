import env

URL_BASE = rf"{env.API_URL}/{env.API_VERSION}"

# Auth
LOGIN = rf"{URL_BASE}/auth/login"
LOGOUT = rf"{URL_BASE}/auth/login"

# Chats
CHATS = rf"{URL_BASE}/chats"
