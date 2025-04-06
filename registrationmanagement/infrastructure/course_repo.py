from core.utils.types import Error
from registrationmanagement.models import Course
from registrationmanagement.utils.types import (
    CourseQuerySetType,
    CourseRegistrationQuerySetType,
)


class CourseRepo:
    @staticmethod
    def get_courses_exlcuding_enrolled_courses(
        enrolled_courses: CourseRegistrationQuerySetType,
    ) -> tuple[CourseQuerySetType, Error]:
        try:
            courses = Course.objects.exclude(
                course_id__in=enrolled_courses.values_list("course_id", flat=True)
            )
            return courses, None
        except Exception as e:
            return None, str(e)
