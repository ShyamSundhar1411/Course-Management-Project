from enum import Enum


class CourseRegistrationResponseMessage(Enum):
    COURSE_REGISTRATION_SUCCESS = "Course registration successful"
    COURSE_REGISTRATION_FAILURE = "Course registration failed"
