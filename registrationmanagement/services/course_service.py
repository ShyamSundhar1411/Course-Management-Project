from core.utils.types import Error
from registrationmanagement.infrastructure import CourseRepo, FacultyRepo
from registrationmanagement.utils.types import (
    CourseQuerySetType,
    CourseRegistrationQuerySetType,
    CourseType,
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

    @staticmethod
    def fetch_courses_by_faculty(user) -> tuple[CourseQuerySetType, Error]:
        courses, error = CourseRepo.get_courses_by_faculty(user)
        if error:
            return None, error
        return courses, error

    @staticmethod
    def create_course(request, course_data) -> tuple[CourseType, Error]:
        faculty, error = FacultyRepo.get_faculty_by_user(request.user)
        if error:
            return None, error
        course_data["primary_instructor"] = faculty
        course, error = CourseRepo.create_course(course_data)
        if error:
            return None, error
        return course, None
