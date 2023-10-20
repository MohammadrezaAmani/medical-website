from django.urls import path
from . import views

urlpatterns = [
    path("profile/", views.doctor_profile, name="patient-profile"),
    path(
        "patients/",
        views.DoctorPatients.as_view(),
        name="doctor-patients",
    ),
    path(
        "sessions/",
        views.DoctorSessions.as_view(),
        name="doctor",
    ),
    path(
        "sessions/<int:pk>/",
        views.DoctorSessionsDetails.as_view(),
        name="doctor-sessions-details",
    ),
    path(
        "exercises/",
        views.DoctorExercises.as_view(),
        name="doctor-exercises",
    ),
    path(
        "exercises/<int:pk>/",
        views.DoctorExerciseDetails.as_view(),
        name="doctor-excercise-details",
    ),
    path("login/", views.DoctorLoginView.as_view(), name="doctor-login"),
    path("me/", views.DoctorMe.as_view(), name="doctor-me"),
    path("add-session/", views.AddSession.as_view(), name="add-session"),
]
