from rest_framework import generics
from .models import Patient
from .serializers import PatientSerializer
from rest_framework.response import Response
from session.serializers import SessionSerializer

class PatientListCreateView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class PatientSessions(generics.RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get(self, request, *args, **kwargs):
        patient = self.get_object()
        sessions = patient.session_set.all()
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)