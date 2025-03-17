import os

# API
API_HOST = os.getenv(key="API_HOST", default="localhost")
API_PORT = os.getenv(key="API_PORT", default="8000")
API_URL = f"{API_HOST}:{API_PORT}"
API_VERSION = os.getenv(key="API_VERSION", default="")
