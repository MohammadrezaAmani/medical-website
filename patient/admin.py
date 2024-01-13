from django.contrib import admin

from .models import Patient


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    """
    Admin class for the Patient model.
    """

    list_display = (
        "name",
        "last_name",
        "user",
        "doctor",
        "gender",
        "birth_date",
    )
    list_filter = ("gender",)
    search_fields = ("name", "last_name", "insurance_number")

    fieldsets = (
        (
            "Personal Information",
            {
                "fields": (
                    "name",
                    "last_name",
                    "user",
                    "doctor",
                    "photo",
                    "bio",
                    "gender",
                    "birth_date",
                )
            },
        ),
        ("Contact Information", {"fields": ("address", "phone_number")}),
        (
            "Insurance Information",
            {
                "fields": (
                    "insurance_number",
                    "insurance_company",
                    "injury_date",
                    "injury_description",
                    "injury_type",
                )
            },
        ),
        ("Medical Documents", {"fields": ("medical_documents",)}),
    )

    def get_user_full_name(self, obj):
        """
        Returns the full name of the user associated with the patient object.

        Args:
            obj: The patient object.

        Returns:
            The full name of the user associated with the patient object.
        """
        return obj.user.get_full_name()

    get_user_full_name.short_description = "User Full Name"
    get_user_full_name.admin_order_field = "user__first_name"


# admin.site.site_header = "Your Admin Site Header"  # Customize the admin site header
# admin.site.site_title = "Your Admin Site Title"  # Customize the admin site title
