from django.db.models.query import QuerySet
from rest_framework import generics

from doctor.models import Doctor
from patient.models import Patient
from .models import Prescription, Drug
from .serializers import PrescriptionSerializer, DrugSerializer
from utils.auth import (
    get_doctor_from_token,
    get_user_from_token,
    get_patient_from_token,
)


class PrescriptionListCreateView(generics.ListCreateAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

    def get_queryset(self) -> QuerySet:
        doctor = get_doctor_from_token(self.request)
        if isinstance(doctor,Doctor):
            return Prescription.objects.filter(patient__doctor=doctor)
        patient = get_user_from_token(self.request)
        if isinstance(patient,Patient):
            patient = get_patient_from_token(self.request)
            return Prescription.objects.filter(patient=patient)
        else:
            return Prescription.objects.none()


class PrescriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

    def get_queryset(self) -> QuerySet:
        doctor = get_doctor_from_token(self.request)
        if isinstance(doctor,Doctor):
            return Prescription.objects.filter(patient__doctor=doctor)
        patient = get_user_from_token(self.request)
        if isinstance(patient,Patient):
            patient = get_patient_from_token(self.request)
            return Prescription.objects.filter(patient=patient)
        else:
            return Prescription.objects.none()


class DrugListCreateView(generics.ListCreateAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer

    def get_queryset(self) -> QuerySet:
        doctor = get_doctor_from_token(self.request)
        if isinstance(doctor,Doctor):
            return Drug.objects.filter(patient__doctor=doctor)
        patient = get_user_from_token(self.request)
        if isinstance(patient,Patient):
            patient = get_patient_from_token(self.request)
            return Drug.objects.filter(patient=patient)
        else:
            return Drug.objects.none()


class DrugDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer

    def get_queryset(self) -> QuerySet:
        doctor = get_doctor_from_token(self.request)
        if isinstance(doctor,Doctor):
            return Drug.objects.filter(patient__doctor=doctor)
        patient = get_user_from_token(self.request)
        if isinstance(patient,Patient):
            patient = get_patient_from_token(self.request)
            return Drug.objects.filter(patient=patient)
        else:
            return Drug.objects.none()
