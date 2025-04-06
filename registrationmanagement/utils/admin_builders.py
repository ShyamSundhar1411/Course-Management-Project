from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    """
    Custom admin configuration for the User model.

    This admin class extends the default UserAdmin provided by Django
    and customizes the display and organization of fields in the Django admin.
    """

    list_display = (
        "username",
        "email",
        "phone_number",
        "is_contact_verified",
        "is_email_verified",
        "is_staff",
        "role",
    )

    fieldsets = list(UserAdmin.fieldsets) + [
        (
            "Profile Fields",
            {
                "fields": (
                    "phone_number",
                    "is_contact_verified",
                    "is_email_verified",
                    "gender",
                    "role",
                ),
            },
        ),
    ]
