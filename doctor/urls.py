from django.urls import path
from . import views

urlpatterns = [
    path("doctors/", views.DoctorDetailView.as_view(), name="doctor-detail"),
    path(
        "doctors/exercises/",
        views.DoctorExercises.as_view(),
        name="doctor-exercises",
    ),
    path(
        "doctors/patients/",
        views.DoctorPatients.as_view(),
        name="doctor-patients",
    ),
    path(
        "doctors/sessions/",
        views.DoctorSessions.as_view(),
        name="doctor-sessions",
    ),
    path("login/", views.DoctorLoginView.as_view(), name="doctor-login"),
    path("me/", views.DoctorMe.as_view(), name="doctor-me"),
]
