import uuid

from django.db import models


class Student(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, unique=True, default=uuid.uuid4
    )
    registration_number = models.CharField(max_length=20, unique=True)
    branch = models.CharField(max_length=50)
    school = models.CharField(max_length=100)
    user = models.OneToOneField("registrationmanagement.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.registration_number

    class Meta:
        app_label = "registrationmanagement"


class Faculty(models.Model):
    id = models.UUIDField(
        primary_key=True, editable=False, unique=True, default=uuid.uuid4
    )
    employee_id = models.CharField(max_length=20, unique=True)
    department = models.CharField(max_length=50)
    school = models.CharField(max_length=100)
    user = models.OneToOneField("registrationmanagement.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_id

    class Meta:
        app_label = "registrationmanagement"
