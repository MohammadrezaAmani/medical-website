"""
This module defines Django views for the Session model.

It provides two views:
- SessionListCreateView: a view that allows to list and create sessions.
- SessionDetailView: a view that allows to retrieve, update and delete a session.

Both views use the Session model and the SessionSerializer to handle requests and responses.
"""

from exercise.serializers import ExerciseSerializer
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Session
from .serializers import SessionSerializer


class SessionListCreateView(generics.ListCreateAPIView):
    """
    A view that allows to list and create sessions.

    Attributes:
        queryset: A queryset of all Session objects.
        serializer_class: The serializer class to use for Session objects.
    """

    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class SessionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    A view that allows to retrieve, update and delete a session.

    Attributes:
        queryset: A queryset of all Session objects.
        serializer_class: The serializer class to use for Session objects.
    """

    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    @action(detail=True, methods=["get"])
    def get_session_exercises(self, request, pk=None):
        session = self.get_object()
        exercises = (
            session.prescription.first().exercises.all()
        )  # Assuming a session has one prescription
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)
