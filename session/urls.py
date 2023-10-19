from django.urls import path
from .views import SessionListCreateView, SessionDetailView

urlpatterns = [
    path("sessions/", SessionListCreateView.as_view(), name="session-list"),
    path("sessions/<int:pk>/", SessionDetailView.as_view(), name="session-detail"),
]
