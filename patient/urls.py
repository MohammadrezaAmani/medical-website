"""
This module defines the URL patterns for the patient app.

The urlpatterns variable is a list of URL patterns. Each URL pattern is defined using the path() function
from the django.urls module. The path() function takes three arguments:
- route: A string that contains a URL pattern.
- view: The view function that should be called when the URL pattern is matched.
- name: A unique name for the URL pattern.

This module defines the following URL patterns:
- /patient/exercises/ : The PatientExercises view is called when this URL pattern is matched.
- /patient/sessions/ : The PatientSessions view is called when this URL pattern is matched.
- /login/ : The PatientLoginView view is called when this URL pattern is matched.
- /patient/profile/ : The patient_profile view is called when this URL pattern is matched.
"""
from django.urls import path
from . import views

urlpatterns = [
    path(
        "exercises/",
        views.PatientExercises.as_view(),
        name="patient-exercises",
    ),
    path(
        "session/",
        views.PatientSessions.as_view(),
        name="patient-sessions",
    ),
    path(
        "sessions/",
        views.PatientSessions2.as_view(),
        name="patient-sessions",
    ),
    path('session/<int:session_id>/exercises/', views.patient_session_exercises, name='patient_session_exercises'),

    path("login/", views.PatientLoginView.as_view(), name="patient-login"),
    # path("me/", views.PatientMe.as_view(), name="patient-me"),
    # pk
    path("profile/", views.patient_profile, name="patient-profile"),
]
