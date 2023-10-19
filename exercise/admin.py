from django.contrib import admin

# Register your models here.
from .models import (
    Equipment,
    Goal,
    Displacement,
    PlacementPosition,
    Exercise,
)

admin.site.register(Exercise)
admin.site.register(Equipment)
admin.site.register(Goal)
admin.site.register(Displacement)
admin.site.register(PlacementPosition)
