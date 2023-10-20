# from rest_framework import generics
# from .models import Prescription, Drug
# from .serializers import PrescriptionSerializer, DrugSerializer


# class PrescriptionListCreateView(generics.ListCreateAPIView):
#     queryset = Prescription.objects.all()
#     serializer_class = PrescriptionSerializer


# class PrescriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Prescription.objects.all()
#     serializer_class = PrescriptionSerializer


# class DrugListCreateView(generics.ListCreateAPIView):
#     queryset = Drug.objects.all()
#     serializer_class = DrugSerializer


# class DrugDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Drug.objects.all()
#     serializer_class = DrugSerializer

# views.py in patient app
from rest_framework import generics
from patient.models import Patient
from patient.serializers import PatientSerializer
from rest_framework.permissions import IsAuthenticated


class PatientListView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]


class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]
