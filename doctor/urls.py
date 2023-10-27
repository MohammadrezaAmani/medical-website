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
        "patients/<int:pk>",
        views.DoctorPatientDetails.as_view(),
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
    path("add-patient/", views.AddPatient.as_view(), name="add-patient"),
    path("add-exercise/", views.AddExercise.as_view(), name="add-exercise"),
    path("session-date/<str:date>/", views.SessionDate.as_view(), name="session-date"),
]

"""
This module defines the URL patterns for the doctor app.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
    
The following URL patterns are defined:
    - profile/ : maps to views.doctor_profile
    - patients/ : maps to views.DoctorPatients.as_view()
    - patients/<int:pk> : maps to views.DoctorPatientDetails.as_view()
    - sessions/ : maps to views.DoctorSessions.as_view()
    - sessions/<int:pk>/ : maps to views.DoctorSessionsDetails.as_view()
    - exercises/ : maps to views.DoctorExercises.as_view()
    - exercises/<int:pk>/ : maps to views.DoctorExerciseDetails.as_view()
    - login/ : maps to views.DoctorLoginView.as_view()
    - me/ : maps to views.DoctorMe.as_view()
    - add-session/ : maps to views.AddSession.as_view()
    - add-patient/ : maps to views.AddPatient.as_view()
    - add-exercise/ : maps to views.AddExercise.as_view()
    - session-date/<str:date>/ : maps to views.SessionDate.as_view()
"""
