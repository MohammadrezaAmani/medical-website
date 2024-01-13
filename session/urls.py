from django.urls import path

from .views import SessionDetailView, SessionListCreateView

urlpatterns = [
    path("sessions/", SessionListCreateView.as_view(), name="session-list"),
    path("sessions/<int:pk>/", SessionDetailView.as_view(), name="session-detail"),
    path(
        "sessions/<int:pk>/exercises/",
        SessionDetailView.as_view(),
        name="session-exercises",
    ),
]
