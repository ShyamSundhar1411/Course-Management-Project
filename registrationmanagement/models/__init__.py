from .course_models import Course
from .profile_models import Faculty, Student
from .registration_models import CourseRegistration
from .user_models import User

__all__ = [
    "User",
    "Student",
    "Faculty",
    "Course",
    "CourseRegistration",
]
