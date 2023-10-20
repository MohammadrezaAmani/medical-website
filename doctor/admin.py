from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "last_name",
        "user",
        "gender",
        "birth_date",
        "medical_system_code",
        "is_active",
        "is_doctor",
    )
    list_filter = ("gender", "is_active", "is_doctor")
    search_fields = ("name", "last_name", "medical_system_code")

    fieldsets = (
        (
            "Personal Information",
            {
                "fields": (
                    "name",
                    "last_name",
                    "user",
                    "photo",
                    "bio",
                    "gender",
                    "birth_date",
                    "medical_system_code",
                )
            },
        ),
        ("Contact Information", {"fields": ("address", "phone_number")}),
        ("Status", {"fields": ("is_active", "is_doctor")}),
    )
    readonly_fields = ("created_at", "updated_at")

    def get_user_full_name(self, obj):
        return obj.user.get_full_name()

    get_user_full_name.short_description = "User Full Name"
    get_user_full_name.admin_order_field = "user__first_name"


# admin.site.site_header = "Your Admin Site Header"  # Customize the admin site header
# admin.site.site_title = "Your Admin Site Title"  # Customize the admin site title
