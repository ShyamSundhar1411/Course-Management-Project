from django import forms
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError

from registrationmanagement.utils import GENDER_CHOICES


class StudentLoginForm(forms.Form):
    registration_number = forms.CharField(label="Registration Number", max_length=20)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        fields = ["registration_number", "password"]


class FacultyLoginForm(forms.Form):
    employee_id = forms.CharField(label="Employee ID", max_length=20)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

    class Meta:
        fields = ["employee_id", "password"]


class StudentSignUpForm(forms.Form):
    username = forms.CharField(label="Username")
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    phone_number = forms.CharField(label="Phone Number")
    branch = forms.CharField(label="Branch")
    school = forms.CharField(label="school")
    gender = forms.ChoiceField(label="Gender", choices=GENDER_CHOICES)
    registration_number = forms.CharField(label="Registration Number", max_length=20)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match.")
        try:
            validate_password(password)
        except DjangoValidationError as exc:
            self.add_error("password", exc)
