from enum import Enum


class AuthResponseMessage(Enum):
    INVALID_CREDENTIALS = "Invalid credentials"
    LOGIN_SUCCESS = "Logged in successfully"
    REGISTRATION_SUCCESSFUL = "Registration successful"
    REGISTRATION_UNSUCCESSFUL = "Registration unsuccessful"
