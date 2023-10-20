from django.urls import path
from . import views

urlpatterns = [
    path(
        "patient/exercises/",
        views.PatientExercises.as_view(),
        name="patient-exercises",
    ),
    path(
        "patient/sessions/",
        views.PatientSessions.as_view(),
        name="patient-sessions",
    ),
    path("login/", views.PatientLoginView.as_view(), name="patient-login"),
    # path("me/", views.PatientMe.as_view(), name="patient-me"),
    # pk
    path("patient/profile/", views.patient_profile, name="patient-profile"),
]
