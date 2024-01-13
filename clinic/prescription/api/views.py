from django.db.models.query import QuerySet
from doctor.models import Doctor
from patient.models import Patient
from rest_framework import generics
from utils.auth import (
    get_doctor_from_token,
    get_patient_from_token,
    get_user_from_token,
)

from ..models import Prescription
from .serializers import PrescriptionSerializer


class PrescriptionListCreateView(generics.ListCreateAPIView):
    """
    API view for listing and creating prescriptions.

    Only authorized doctors and patients can access this view.
    Doctors can only access prescriptions that belong to their patients.
    Patients can only access their own prescriptions.
    """

    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

    def get_queryset(self) -> QuerySet:
        """
        Returns a queryset of prescriptions based on the user's role.

        If the user is a doctor, returns prescriptions related to their patients.
        If the user is a patient, returns their own prescriptions.
        """
        doctor = get_doctor_from_token(self.request)
        if isinstance(doctor, Doctor):
            return Prescription.objects.filter(patient__doctor=doctor)
        patient = get_user_from_token(self.request)
        if isinstance(patient, Patient):
            patient = get_patient_from_token(self.request)
            return Prescription.objects.filter(patient=patient)
        else:
            return Prescription.objects.none()


class PrescriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    A view for retrieving, updating and deleting a prescription object.

    Only authorized doctors and patients can access this view.
    """

    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

    def get_queryset(self) -> QuerySet:
        """
        Returns a queryset of prescriptions based on the user's role.

        If the user is a doctor, returns prescriptions related to their patients.
        If the user is a patient, returns their own prescriptions.
        """
        doctor = get_doctor_from_token(self.request)
        if isinstance(doctor, Doctor):
            return Prescription.objects.filter(patient__doctor=doctor)
        patient = get_user_from_token(self.request)
        if isinstance(patient, Patient):
            patient = get_patient_from_token(self.request)
            return Prescription.objects.filter(patient=patient)
        else:
            return Prescription.objects.none()

    def get(
        self,
    ):
        print(self.request)
        return self.get_queryset().filter(id=["pk"])


# class DrugListCreateView(generics.ListCreateAPIView):
#     """
#     API view for listing and creating drugs.

#     Only authorized doctors and patients can access this view.
#     Doctors can only access drugs that belong to their patients.
#     Patients can only access their own drugs.
#     """

#     queryset = Drug.objects.all()
#     serializer_class = DrugSerializer

#     def get_queryset(self) -> QuerySet:
#         """
#         Returns the queryset of drugs based on the user type (doctor or patient).
#         """
#         doctor = get_doctor_from_token(self.request)
#         if isinstance(doctor, Doctor):
#             return Drug.objects.filter(patient__doctor=doctor)
#         patient = get_user_from_token(self.request)
#         if isinstance(patient, Patient):
#             patient = get_patient_from_token(self.request)
#             return Drug.objects.filter(patient=patient)
#         else:
#             return Drug.objects.none()


# class DrugDetailView(generics.RetrieveUpdateDestroyAPIView):
#     """
#     A view for retrieving, updating and deleting a drug object.

#     Only authorized doctors and patients can access this view.
#     Doctors can only access drugs that belong to their patients.
#     Patients can only access their own drugs.
#     """

#     queryset = Drug.objects.all()
#     serializer_class = DrugSerializer

#     def get_queryset(self) -> QuerySet:
#         doctor = get_doctor_from_token(self.request)
#         if isinstance(doctor, Doctor):
#             return Drug.objects.filter(patient__doctor=doctor)
#         patient = get_user_from_token(self.request)
#         if isinstance(patient, Patient):
#             patient = get_patient_from_token(self.request)
#             return Drug.objects.filter(patient=patient)
#         else:
#             return Drug.objects.none()
