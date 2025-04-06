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

    @staticmethod
    def create_course_registration(
        registration_data: dict,
    ) -> tuple[CourseRegistration, Error]:
        try:
            course_registration = CourseRegistration.objects.create(**registration_data)
            return course_registration, None
        except Exception as e:
            return None, str(e)
