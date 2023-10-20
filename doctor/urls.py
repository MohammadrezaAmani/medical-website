from django.urls import path
from . import views

urlpatterns = [
    path("doctors/<int:pk>/", views.DoctorDetailView.as_view(), name="doctor-detail"),
    path(
        "doctors/<int:pk>/exercises/",
        views.DoctorExercises.as_view(),
        name="doctor-exercises",
    ),
    path(
        "doctors/<int:pk>/patients/",
        views.DoctorPatients.as_view(),
        name="doctor-patients",
    ),
    path(
        "doctors/<int:pk>/sessions/",
        views.DoctorSessions.as_view(),
        name="doctor-sessions",
    ),
    path("login/", views.DoctorLoginView.as_view(), name="doctor-login"),
    path("me/", views.DoctorMe.as_view(), name="doctor-me"),
]
