from core.utils.types import Error
from registrationmanagement.infrastructure import CourseRepo
from registrationmanagement.utils.types import (
    CourseQuerySetType,
    CourseRegistrationQuerySetType,
)


class CourseService:
    @staticmethod
    def fetch_courses(
        enrolled_courses: CourseRegistrationQuerySetType,
    ) -> tuple[CourseQuerySetType, Error]:
        courses, error = CourseRepo.get_courses_exlcuding_enrolled_courses(
            enrolled_courses
        )
        if error:
            return None, error
        return courses, error
