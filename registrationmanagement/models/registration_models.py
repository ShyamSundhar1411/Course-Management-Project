import uuid

from django.db import models


class CourseRegistration(models.Model):
    registration_id = models.UUIDField(
        primary_key=True, editable=False, unique=True, default=uuid.uuid4
    )
    student = models.ForeignKey(
        "registrationmanagement.Student", on_delete=models.CASCADE
    )
    course = models.ForeignKey(
        "registrationmanagement.Course",
        on_delete=models.CASCADE,
        related_name="course_registration",
    )
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.registration_id)

    class Meta:
        app_label = "registrationmanagement"
