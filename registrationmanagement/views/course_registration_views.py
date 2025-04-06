from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from registrationmanagement.services import CourseRegistrationService
from registrationmanagement.utils import CourseRegistrationResponseMessage


@login_required
def enroll_course(request, course_id):
    if request.method == "POST":
        _, error = CourseRegistrationService.enroll_course(request.user, course_id)
        if error:
            messages.error(request, error)
            return redirect("home")
        messages.success(
            request, CourseRegistrationResponseMessage.COURSE_REGISTRATION_SUCCESS.value
        )
        return redirect("home")
    return redirect("home")
