from django.contrib import admin

from .models import (
    Displacement,
    Equipment,
    Exercise,
    Goal,
    Organ,
    PlacementPosition,
    Target,
)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Displacement)
class DisplacementAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(PlacementPosition)
class PlacementPositionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Target)
class TargetAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Organ)
class OrganAdmin(admin.ModelAdmin):
    list_display = ("name", "photo")
    search_fields = ("name",)
    list_filter = ("name",)


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
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
