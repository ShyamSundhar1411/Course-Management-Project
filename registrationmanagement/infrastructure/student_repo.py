from core.utils.types import Error
from registrationmanagement.models import Student
from registrationmanagement.utils.types import StudentType


class StudentRepo:
    @staticmethod
    def get_student_by_registration_number(
        registration_number: str,
    ) -> tuple[StudentType, Error]:
        try:
            student = Student.objects.get(registration_number=registration_number)
            return student, None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def get_student_by_user(user) -> tuple[StudentType, Error]:
        try:
            student = Student.objects.get(user=user)
            return student, None
        except Exception as e:
            return None, str(e)
