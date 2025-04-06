from django.contrib.auth import authenticate, login

from core.utils.types import Error
from registrationmanagement.infrastructure.student_repo import StudentRepo
from registrationmanagement.infrastructure.types import StudentType, UserType
from registrationmanagement.utils.auth_response_message import AuthResponseMessage


class AuthService:
    @staticmethod
    def authenticate_user(request: dict, user_data: dict) -> tuple[UserType, Error]:
        user = authenticate(
            request, username=user_data["user"].username, password=user_data["password"]
        )
        if user is None:
            return None, AuthResponseMessage.INVALID_CREDENTIALS.value
        login(request, user)
        return user, None

    @staticmethod
    def login_student(reqeust: dict, data: dict) -> tuple[StudentType, Error]:
        student, error = StudentRepo.get_student_by_registration_number(
            data["registration_number"]
        )
        if error:
            return None, AuthResponseMessage.INVALID_CREDENTIALS.value
        user_data = {"user": student.user, "password": data["password"]}
        user, error = AuthService.authenticate_user(reqeust, user_data)
        if error:
            return None, error
        return user, None
