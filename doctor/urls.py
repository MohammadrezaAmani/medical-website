from django.urls import path
from .views import (
    DoctorListCreateView,
    DoctorDetailView,
    DoctorExercises,
    DoctorPatients,
    DoctorSessions,
)

urlpatterns = [
    path("", DoctorListCreateView.as_view(), name="doctor-list"),
    path("<int:pk>/", DoctorDetailView.as_view(), name="doctor-detail"),
    path("<int:pk>/exercises/", DoctorExercises.as_view(), name="doctor-exercises"),
    path("<int:pk>/patients/", DoctorPatients.as_view(), name="doctor-patients"),
    path("<int:pk>/sessions/", DoctorSessions.as_view(), name="doctor-sessions"),
]
