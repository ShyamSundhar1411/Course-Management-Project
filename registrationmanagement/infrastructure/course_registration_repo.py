from core.utils.types import Error
from registrationmanagement.models import CourseRegistration, User
from registrationmanagement.utils.types import CourseRegistrationQuerySetType


class CourseRegistrationRepo:
    @staticmethod
    def get_enrolled_courses_by_student(
        user: User,
    ) -> tuple[CourseRegistrationQuerySetType, Error]:
        try:
            enrolled_courses = CourseRegistration.objects.filter(student__user=user)
            return enrolled_courses, None
        except Exception as e:
            return None, str(e)
