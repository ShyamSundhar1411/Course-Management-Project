import uuid

from django.db import models


class Course(models.Model):
    course_id = models.UUIDField(
        primary_key=True, editable=False, unique=True, default=uuid.uuid4
    )
    course_name = models.CharField(max_length=100)
    course_description = models.CharField(max_length=500)
    course_code = models.CharField(max_length=20, unique=True)
    primary_instructor = models.ForeignKey(
        "registrationmanagement.Faculty", on_delete=models.CASCADE
    )
    instructors = models.ManyToManyField(
        "registrationmanagement.Faculty", related_name="instructors"
    )

    def __str__(self):
        string_representation = f"{self.course_name} - ({self.course_code})"
        return string_representation

    class Meta:
        app_label = "registrationmanagement"
