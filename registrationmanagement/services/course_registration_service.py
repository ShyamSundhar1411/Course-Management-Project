from core.utils.types import Error
from registrationmanagement.infrastructure import (
    CourseRegistrationRepo,
    CourseRepo,
    StudentRepo,
)
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

    @staticmethod
    def enroll_course(user: User, course_id: str) -> tuple[bool, Error]:
        student, error = StudentRepo.get_student_by_user(user)
        if error:
            return None, error
        course, error = CourseRepo.get_course_by_id(course_id)
        if error:
            return None, error
        registration_data = {
            "student": student,
            "course": course,
        }
        _, error = CourseRegistrationRepo.create_course_registration(registration_data)
        if error:
            return False, error
        return True, None
