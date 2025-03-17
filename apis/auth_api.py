from apis.api_wrapper import ApiWrapper


def login(email: str, password: str) -> bool:
    return ApiWrapper().login(email=email, password=password)


def logout():
    ApiWrapper().logout()
