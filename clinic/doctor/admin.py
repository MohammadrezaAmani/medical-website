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
                    "last_name",
                    "password",
                    "email",
                    "photo",
                    "bio",
                    "gender",
                    "birth_date",
                    "medical_system_code",
                )
            },
        ),
        ("Contact Information", {"fields": ("address", "username")}),
    )
    readonly_fields = ("created_at", "updated_at")

    def get_user_full_name(self, obj):
        return obj.user.get_full_name()

    get_user_full_name.short_description = "User Full Name"
    get_user_full_name.admin_order_field = "user__first_name"
