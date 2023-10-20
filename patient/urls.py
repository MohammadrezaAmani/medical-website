from django.urls import path
from .views import PatientListCreateView, PatientDetailView

urlpatterns = [
    path("patients/", PatientListCreateView.as_view(), name="patient-list"),
    path("patients/<int:pk>/", PatientDetailView.as_view(), name="patient-detail"),
]

# urls.py in patient app
from django.urls import path
from patient.views import PatientLoginView

urlpatterns += [
    # ... other URLs
    path("api/patient-login/", PatientLoginView.as_view(), name="patient-login"),
]
