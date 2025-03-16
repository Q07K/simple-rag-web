import json
from typing import Any, Self

import requests

from apis import api_url


class ApiWrapper:
    _instance = None

    def __new__(cls, *args, **kwargs) -> Self:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, "cookies"):
            self.cookies = None

    def login(self, email: str, password: str) -> bool:
        with requests.Session() as c:
            response = c.post(
                url=api_url.LOGIN,
                data={
                    "username": email,
                    "password": password,
                },
            )
            if response.status_code == 200:
                self.cookies = c.cookies
                return True
        return False

    def logout(self) -> None:
        with requests.Session() as c:
            c.post(url=api_url.LOGOUT, cookies=self.cookies)

    def get(self, url: str) -> Any | None:
        with requests.Session() as c:
            response = c.get(
                url=url,
                cookies=self.cookies,
            )
        if response.status_code == 200:
            return json.loads(response.text)

    def post(self, url: str, data: Any) -> Any | None:
        with requests.Session() as c:
            response = c.post(
                url=url,
                data=data,
                cookies=self.cookies,
            )
        if response.status_code == 200:
            return json.loads(response.text)

    def delete(self, url: str) -> Any | None:
        with requests.Session() as c:
            response = c.post(
                url=url,
                cookies=self.cookies,
            )
        if response.status_code == 200:
            return json.loads(response.text)
