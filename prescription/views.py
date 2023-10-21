from django.db.models.query import QuerySet
from rest_framework import generics
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
        user = get_user_from_token(self.request)
        if user.is_doctor:
            doctor = get_doctor_from_token(self.request)
            return Prescription.objects.filter(patient__doctor=doctor)
        elif user.is_patient:
            patient = get_patient_from_token(self.request)
            return Prescription.objects.filter(patient=patient)
        else:
            return Prescription.objects.none()


class PrescriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

    def get_queryset(self) -> QuerySet:
        user = get_user_from_token(self.request)
        if user.is_doctor:
            doctor = get_doctor_from_token(self.request)
            return Prescription.objects.filter(patient__doctor=doctor)
        elif user.is_patient:
            patient = get_patient_from_token(self.request)
            return Prescription.objects.filter(patient=patient)
        else:
            return Prescription.objects.none()


class DrugListCreateView(generics.ListCreateAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer

    def get_queryset(self) -> QuerySet:
        user = get_user_from_token(self.request)
        if user.is_doctor:
            doctor = get_doctor_from_token(self.request)
            return Drug.objects.filter(patient__doctor=doctor)
        elif user.is_patient:
            patient = get_patient_from_token(self.request)
            return Drug.objects.filter(patient=patient)
        else:
            return Drug.objects.none()


class DrugDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer

    def get_queryset(self) -> QuerySet:
        user = get_user_from_token(self.request)
        if user.is_doctor:
            doctor = get_doctor_from_token(self.request)
            return Drug.objects.filter(patient__doctor=doctor)
        elif user.is_patient:
            patient = get_patient_from_token(self.request)
            return Drug.objects.filter(patient=patient)
        else:
            return Drug.objects.none()
