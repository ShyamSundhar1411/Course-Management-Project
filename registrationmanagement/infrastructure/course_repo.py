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

    @staticmethod
    def get_course_by_id(course_id: int) -> tuple[Course, Error]:
        try:
            course = Course.objects.get(course_id=course_id)
            return course, None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def get_courses_by_faculty(user) -> tuple[CourseQuerySetType, Error]:
        try:
            courses = Course.objects.filter(primary_instructor__user=user)
            return courses, None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def create_course(course_data) -> tuple[Course, Error]:
        try:
            course = Course.objects.create(**course_data)
            course.instructors.add(course.primary_instructor)
            course.save()
            return course, None
        except Exception as e:
            return None, str(e)
