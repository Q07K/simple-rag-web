from email_validator import EmailNotValidError, validate_email


def none_validator(text: str, /) -> bool:
    if text is None:
        return False
    if text == "":
        return False
    return True


def email_validator(email: str) -> bool:
    if none_validator(email):
        try:
            validate_email(email)
            return True
        except EmailNotValidError:
            return False
    return False


def password_validator(password: str) -> bool:
    if none_validator(password):
        return True
    return False
