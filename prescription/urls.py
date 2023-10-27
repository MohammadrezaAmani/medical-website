from django.urls import path
from .views import (
    PrescriptionListCreateView,
    PrescriptionDetailView,
    # DrugListCreateView,
    # DrugDetailView,
)

"""
This module defines the URL patterns for the prescription app.
"""
urlpatterns = [
    # Prescription URLs
    path(
        "prescriptions/", PrescriptionListCreateView.as_view(), name="prescription-list"
    ),
    path(
        "prescriptions/<int:pk>/",
        PrescriptionDetailView.as_view(),
        name="prescription-detail",
    ),
    # Drug URLs
    # path("drugs/", DrugListCreateView.as_view(), name="drug-list"),
    # path("drugs/<int:pk>/", DrugDetailView.as_view(), name="drug-detail"),
]
