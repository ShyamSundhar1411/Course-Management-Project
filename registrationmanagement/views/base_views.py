from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from registrationmanagement.services import CourseRegistrationService, CourseService


@login_required
def home(request):
    if request.user.role == "Student":
        (
            enrolled_courses,
            error,
        ) = CourseRegistrationService.fetch_enrolled_courses_by_students(request.user)
        if error:
            messages.error(request, error)
            return render(request, "registrationmanagement/home.html")
        courses, error = CourseService.fetch_courses(enrolled_courses)
        if error:
            messages.error(request, error)
            return render(request, "registrationmanagement/home.html")

        return render(
            request,
            "registrationmanagement/home.html",
            {"enrolled_courses": enrolled_courses, "courses": courses},
        )
    return render(request, "registrationmanagement/home.html")
