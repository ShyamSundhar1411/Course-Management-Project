from django.contrib.auth import authenticate, login
from django.db import transaction

from core.utils.types import Error
from registrationmanagement.infrastructure.faculty_repo import FacultyRepo
from registrationmanagement.infrastructure.student_repo import StudentRepo
from registrationmanagement.infrastructure.user_repo import UserRepo
from registrationmanagement.utils.auth_response_message import AuthResponseMessage
from registrationmanagement.utils.types import FacultyType, StudentType, UserType


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
        _, error = AuthService.authenticate_user(reqeust, user_data)
        if error:
            return None, error
        return student, None

    @staticmethod
    def login_faculty(request: dict, data: dict) -> tuple[FacultyType, Error]:
        faculty, error = FacultyRepo.get_faculty_by_employee_id(data["employee_id"])
        if error:
            return None, AuthResponseMessage.INVALID_CREDENTIALS.value
        user_data = {"user": faculty.user, "password": data["password"]}
        _, error = AuthService.authenticate_user(request, user_data)
        if error:
            return None, error
        return faculty, None

    @staticmethod
    def register_student(request: dict, data: dict) -> tuple[StudentType, Error]:
        try:
            with transaction.atomic():
                user_data = {
                    "username": data["username"],
                    "password": data["password"],
                    "first_name": data["first_name"],
                    "last_name": data["last_name"],
                    "gender": data["gender"],
                    "email": data["email"],
                    "role": "Student",
                    "phone_number": data["phone_number"],
                }
                user, error = UserRepo.create_user(user_data)
                if error:
                    raise transaction.TransactionManagementError(error)
                student_data = {
                    "user": user,
                    "registration_number": data["registration_number"],
                    "school": data["school"],
                    "branch": data["branch"],
                }
                student, error = StudentRepo.create_student(student_data)
                if error:
                    raise transaction.TransactionManagementError(error)
                login(request, user)
                return student, None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def register_faculty(request: dict, data: dict) -> tuple[FacultyType, Error]:
        try:
            with transaction.atomic():
                user_data = {
                    "username": data["username"],
                    "password": data["password"],
                    "first_name": data["first_name"],
                    "last_name": data["last_name"],
                    "gender": data["gender"],
                    "email": data["email"],
                    "role": "Faculty",
                    "phone_number": data["phone_number"],
                }
                user, error = UserRepo.create_user(user_data)
                if error:
                    raise transaction.TransactionManagementError(error)
                faculty_data = {
                    "user": user,
                    "employee_id": data["employee_id"],
                    "school": data["school"],
                }
                faculty, error = FacultyRepo.create_faculty(faculty_data)
                if error:
                    raise transaction.TransactionManagementError(error)

                login(request, user)
                return faculty, None
        except Exception as e:
            return None, str(e)
