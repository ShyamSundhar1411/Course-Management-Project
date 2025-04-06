from core.utils.types import Error
from registrationmanagement.models import Faculty
from registrationmanagement.utils.types import FacultyType


class FacultyRepo:
    @staticmethod
    def get_faculty_by_employee_id(employee_id: str) -> tuple[FacultyType, Error]:
        try:
            faculty = Faculty.objects.get(employee_id=employee_id)
            return faculty, None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def get_faculty_by_user(user) -> tuple[FacultyType, Error]:
        try:
            faculty = Faculty.objects.get(user=user)
            return faculty, None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def create_faculty(faculty_data) -> tuple[FacultyType, Error]:
        try:
            faculty = Faculty.objects.create(**faculty_data)
            return faculty, None
        except Exception as e:
            return None, str(e)
