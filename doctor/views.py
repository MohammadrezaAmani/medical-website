from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer
from exercise.serializers import ExerciseSerializer
from rest_framework.response import Response
from patient.serializers import PatientSerializer
from session.serializers import SessionSerializer


class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorExercises(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def get(self, request, *args, **kwargs):
        doctor = self.get_object()
        exercises = doctor.exercise_set.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)


class DoctorPatients(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def get(self, request, *args, **kwargs):
        doctor = self.get_object()
        patients = doctor.patient_set.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)


class DoctorSessions(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def get(self, request, *args, **kwargs):
        doctor = self.get_object()
        sessions = doctor.session_set.all()
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)
