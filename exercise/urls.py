"""
This module contains the URL patterns for the exercise app.

The urlpatterns variable is a list of URL patterns. Each URL pattern is defined using the path() function
from Django's urls module. The path() function takes two required arguments: route and view, and several
optional arguments. The route argument is a string that contains a URL pattern. The view argument is a
callable that takes a request object as its argument and returns an HTTP response.

This module defines the following URL patterns:
- equipment/ : A URL pattern that maps to EquipmentListCreateView.
- equipment/<int:pk>/ : A URL pattern that maps to EquipmentDetailView.
- goals/ : A URL pattern that maps to GoalListCreateView.
- goals/<int:pk>/ : A URL pattern that maps to GoalDetailView.
- displacements/ : A URL pattern that maps to DisplacementListCreateView.
- displacements/<int:pk>/ : A URL pattern that maps to DisplacementDetailView.
- placement-positions/ : A URL pattern that maps to PlacementPositionListCreateView.
- placement-positions/<int:pk>/ : A URL pattern that maps to PlacementPositionDetailView.
- targets/ : A URL pattern that maps to TargetListCreateView.
- targets/<int:pk>/ : A URL pattern that maps to TargetDetailView.
- organs/ : A URL pattern that maps to OrganListCreateView.
- organs/<int:pk>/ : A URL pattern that maps to OrganDetailView.
- '' : A URL pattern that maps to ExerciseListView.

"""

from django.urls import path
from .views import (
    EquipmentListCreateView,
    EquipmentDetailView,
    GoalListCreateView,
    GoalDetailView,
    DisplacementListCreateView,
    DisplacementDetailView,
    PlacementPositionListCreateView,
    PlacementPositionDetailView,
    TargetListCreateView,
    TargetDetailView,
    OrganListCreateView,
    OrganDetailView,
    ExerciseListView,
)

urlpatterns = [
    # Equipment URLs
    path("equipment/", EquipmentListCreateView.as_view(), name="equipment-list"),
    path("equipment/<int:pk>/", EquipmentDetailView.as_view(), name="equipment-detail"),
    # Goal URLs
    path("goals/", GoalListCreateView.as_view(), name="goal-list"),
    path("goals/<int:pk>/", GoalDetailView.as_view(), name="goal-detail"),
    # Displacement URLs
    path(
        "displacements/", DisplacementListCreateView.as_view(), name="displacement-list"
    ),
    path(
        "displacements/<int:pk>/",
        DisplacementDetailView.as_view(),
        name="displacement-detail",
    ),
    # Placement Position URLs
    path(
        "placement-positions/",
        PlacementPositionListCreateView.as_view(),
        name="placementposition-list",
    ),
    path(
        "placement-positions/<int:pk>/",
        PlacementPositionDetailView.as_view(),
        name="placementposition-detail",
    ),
    # Target URLs
    path("targets/", TargetListCreateView.as_view(), name="target-list"),
    path("targets/<int:pk>/", TargetDetailView.as_view(), name="target-detail"),
    # Organ URLs
    path("organs/", OrganListCreateView.as_view(), name="organ-list"),
    path("organs/<int:pk>/", OrganDetailView.as_view(), name="organ-detail"),
    # Exercise URLs
    path("", ExerciseListView.as_view(), name="exercise-list"),
]
