from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from registrationmanagement.forms import CourseCreationForm
from registrationmanagement.services import CourseService
from registrationmanagement.utils import CourseResponseMessage


@login_required
def course_creation(request):
    if request.user.role != "Faculty":
        return redirect("home")
    if request.method == "POST":
        course_form = CourseCreationForm(request.POST)
        if course_form.is_valid():
            _, error = CourseService.create_course(request, course_form.cleaned_data)
            if error:
                messages.error(request, error)
                return render(
                    request,
                    "registrationmanagement/course_creation.html",
                    {"course_form": course_form},
                )
            messages.success(
                request, CourseResponseMessage.COURSE_CREATED_SUCCESSFULLY.value
            )
            return redirect("home")
    return render(
        request,
        "registrationmanagement/course_creation.html",
        {"course_form": CourseCreationForm()},
    )
