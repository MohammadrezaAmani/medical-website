from django.urls import path
from .views import (
    DoctorDetailView,
    # DoctorExercises,
    # DoctorPatients,
    # DoctorSessions,
)

urlpatterns = [
    path("", DoctorDetailView.as_view(), name="doctor-detail"),
    # path("exercises/", DoctorExercises.as_view(), name="doctor-exercises"),
    # path("patients/", DoctorPatients.as_view(), name="doctor-patients"),
    # path("sessions/", DoctorSessions.as_view(), name="doctor-sessions"),
]

# urls.py in doctor app
from django.urls import path
from doctor.views import DoctorLoginView

urlpatterns += [
    # ... other URLs
    path("doctor-login/", DoctorLoginView.as_view(), name="doctor-login"),
]
