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
    ExerciseListCreateView,
    ExerciseDetailView,
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
    path("exercises/", ExerciseListCreateView.as_view(), name="exercise-list"),
    path("exercises/<int:pk>/", ExerciseDetailView.as_view(), name="exercise-detail"),
]
