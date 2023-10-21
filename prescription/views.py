from rest_framework import generics
from .models import Prescription, Drug
from .serializers import PrescriptionSerializer, DrugSerializer
from doctor.views import (
    get_doctor_from_token,
    get_user_from_token,
    get_patient_from_token,
)


class PrescriptionListCreateView(generics.ListCreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class PrescriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class DrugListCreateView(generics.ListCreateAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer


class DrugDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
