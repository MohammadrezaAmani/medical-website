from django.contrib import admin
from .models import (
    Equipment,
    Goal,
    Displacement,
    PlacementPosition,
    Target,
    Organ,
    Exercise,
)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    """
    Admin class for managing Equipments model in the Django admin panel.

    Attributes:
    - list_display: A tuple of field names to display in the list view of the admin panel.
    - search_fields: A tuple of field names to search for in the admin panel search bar.
    """

    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    """
    Admin class for managing Goal model in the Django admin panel.

    Attributes:
    - list_display: A tuple of field names to display in the list view of the admin panel.
    - search_fields: A tuple of field names to search for in the admin panel search bar.
    """

    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Displacement)
class DisplacementAdmin(admin.ModelAdmin):
    """
    Admin class for managing Displacements model in the Django admin panel.

    Attributes:
    - list_display: A tuple of field names to display in the list view of the admin panel.
    - search_fields: A tuple of field names to search for in the admin panel search bar.
    """

    list_display = ("name",)
    search_fields = ("name",)


@admin.register(PlacementPosition)
class PlacementPositionAdmin(admin.ModelAdmin):
    """
    Admin class for managing Placement Possition model in the Django admin panel.

    Attributes:
    - list_display: A tuple of field names to display in the list view of the admin panel.
    - search_fields: A tuple of field names to search for in the admin panel search bar.
    """

    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    """
    Admin class for managing Target model in the Django admin panel.

    Attributes:
    - list_display: A tuple of field names to display in the list view of the admin panel.
    - search_fields: A tuple of field names to search for in the admin panel search bar.
    """

    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Organ)
class OrganAdmin(admin.ModelAdmin):
    """
    Admin class for the Organ model.

    Attributes:
    - list_display: A tuple of model fields to display in the admin list view.
    - search_fields: A tuple of model fields to enable search functionality in the admin list view.
    - list_filter: A tuple of model fields to enable filtering functionality in the admin list view.
    """

    list_display = ("name", "photo")
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    """
    Admin class for managing Exercise model in the Django admin panel.
    """

    list_display = ("name", "owner", "is_public")
    list_filter = ("owner", "is_public")
    search_fields = ("name", "description")
    filter_horizontal = (
        "placement_position",
        "target",
        "target_organs",
        "displacement",
        "accessories",
    )

    fieldsets = (
        (
            "General Information",
            {
                "fields": (
                    "owner",
                    "name",
                    "description",
                    "instructions",
                    "is_public",
                    "keywords",
                )
            },
        ),
        ("Media", {"fields": ("video", "photo")}),
        (
            "Related Information",
            {
                "fields": (
                    "placement_position",
                    "target",
                    "target_organs",
                    "displacement",
                    "accessories",
                )
            },
        ),
    )


# admin.site.site_header = "Your Admin Site Header"  # Customize the admin site header
# admin.site.site_title = "Your Admin Site Title"  # Customize the admin site title
