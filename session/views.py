"""
This module defines Django views for the Session model.

It provides two views:
- SessionListCreateView: a view that allows to list and create sessions.
- SessionDetailView: a view that allows to retrieve, update and delete a session.

Both views use the Session model and the SessionSerializer to handle requests and responses.
"""

from rest_framework import generics
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
