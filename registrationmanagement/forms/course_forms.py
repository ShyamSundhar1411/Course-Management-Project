from django import forms

from registrationmanagement.models import Course


class CourseCreationForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ["course_name", "course_description", "course_code"]
