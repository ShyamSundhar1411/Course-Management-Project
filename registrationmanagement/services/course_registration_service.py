from core.utils.types import Error
from registrationmanagement.infrastructure import CourseRegistrationRepo
from registrationmanagement.models import User
from registrationmanagement.utils.types import CourseRegistrationQuerySetType


class CourseRegistrationService:
    @staticmethod
    def fetch_enrolled_courses_by_students(
        user: User,
    ) -> tuple[CourseRegistrationQuerySetType, Error]:
        (
            enrolled_courses,
            error,
        ) = CourseRegistrationRepo.get_enrolled_courses_by_student(user)
        if error:
            return None, error
        return enrolled_courses, None
