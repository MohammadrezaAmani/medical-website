from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    """
    Admin view for the Doctor model.
    """
    list_display = (
        "id",
        "name",
        "last_name",
        "user",
        "gender",
        "birth_date",
        "medical_system_code",
    )
    list_filter = ("gender", "birth_date")
    search_fields = ("name", "last_name", "medical_system_code")

    fieldsets = (
        (
            "Personal Information",
            {
                "fields": (
                    "name",
                    "password",
                    "username",
                    "email",
                    "last_name",
                    "photo",
                    "bio",
                    "gender",
                    "birth_date",
                    "medical_system_code",
                )
            },
        ),
        ("Contact Information", {"fields": ("address", "phone_number")}),
    )
    readonly_fields = ("created_at", "updated_at")

    def get_user_full_name(self, obj):
        """
        Returns the full name of the user associated with the doctor object.

        Args:
            obj: Doctor object.

        Returns:
            Full name of the user associated with the doctor object.
        """
        return obj.user.get_full_name()

    get_user_full_name.short_description = "User Full Name"
    get_user_full_name.admin_order_field = "user__first_name"


# admin.site.site_header = "Your Admin Site Header"  # Customize the admin site header
# admin.site.site_title = "Your Admin Site Title"  # Customize the admin site title
