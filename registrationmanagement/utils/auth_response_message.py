from enum import Enum


class AuthResponseMessage(Enum):
    INVALID_CREDENTIALS = "Invalid credentials"
    LOGIN_SUCCESS = "Logged in successfully"
