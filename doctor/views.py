from rest_framework import generics
from .models import Doctor
from .serializers import DoctorSerializer
from exercise.serializers import ExerciseSerializer
from rest_framework.response import Response

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