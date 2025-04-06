from django.urls import path

from registrationmanagement.views import (
    auth_views,
    base_views,
    course_registration_views,
    course_views,
)

urlpatterns = [
    path("", base_views.home, name="home"),
    path("login/student/", auth_views.student_login, name="student_login"),
    path(
        "register/student/",
        auth_views.student_registration,
        name="student_registration",
    ),
    path(
        "register/faculty/",
        auth_views.faculty_registration,
        name="faculty_registration",
    ),
    path("login/faculty/", auth_views.faculty_login, name="faculty_login"),
    path(
        "enroll/<str:course_id>/course",
        course_registration_views.enroll_course,
        name="enroll_course",
    ),
    path("course/create/", course_views.course_creation, name="create_course"),
]
