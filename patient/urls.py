from django.urls import path
from .views import PatientListCreateView, PatientDetailView, PatientLoginView

urlpatterns = [
    path("patients/", PatientListCreateView.as_view(), name="patient-list"),
    path("patients/<int:pk>/", PatientDetailView.as_view(), name="patient-detail"),
]

urlpatterns += [
    # ... other URLs
    path("api/patient-login/", PatientLoginView.as_view(), name="patient-login"),
]
