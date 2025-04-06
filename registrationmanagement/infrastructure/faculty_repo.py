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
