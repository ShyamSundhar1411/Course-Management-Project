import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from registrationmanagement.utils.model_constants import GENDER_CHOICES, ROLE_CHOICES


class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="Student")
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = PhoneNumberField()
    is_contact_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)

    class Meta:
        app_label = "registrationmanagement"
