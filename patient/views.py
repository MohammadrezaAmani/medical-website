from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login
from exercise.serializers import ExerciseSerializer
from patient.serializers import PatientSerializer, PatientLoginSerializer
from patient.models import Patient
from session.serializers import SessionSerializer
from session.models import Session
from rest_framework.decorators import api_view
from doctor.serializers import DoctorSerializer

from doctor.views import (
    get_patient_from_token,
)


class PatientLoginView(APIView):
    serializer_class = PatientLoginSerializer

    def post(self, request):
        print("hear")
        username = request.data.get("username")
        password = request.data.get("password")
        print(username)
        user = authenticate(username=username, password=password)
        print(user, "**************")
        login(request, user)
        doctor = Patient.objects.filter(user=user, is_active=True, is_patient=True)
        patient = Patient.objects.filter(user=user, is_active=True, is_patient=False)
        print("patient")
        if len(doctor) > 0:
            if doctor[0].is_active:
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                        "user_id": user.id,
                        "is_patient": True,
                    }
                )
        elif len(patient) > 0:
            if patient[0].is_active:
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                        "user_id": user.id,
                        "is_patient": False,
                    }
                )
        else:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )


class PatientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get(self, request, *args, **kwargs):
        patient = get_patient_from_token(request)
        if isinstance(patient, Patient):
            serializer = PatientSerializer(patient)
            return Response(serializer.data)
        else:
            return Response({"error": "permission denied"})

    def get_object(self):
        patient = get_patient_from_token(self.request)
        if isinstance(patient, Patient):
            serializer = PatientSerializer(patient)
            return Response(serializer.data)
        else:
            return Response({"error": "permission denied"})

    def delete(self, request, *args, **kwargs):
        patient = get_patient_from_token(request)
        if isinstance(patient, Patient):
            patient.delete()
            return Response({"message": "Patient deleted"})
        else:
            return Response({"error": "permission denied"})

    def patch(self, request, *args, **kwargs):
        patient = get_patient_from_token(request)
        if isinstance(patient, Patient):
            serializer = PatientSerializer(patient, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        else:
            return Response({"error": "permission denied"})


class PatientExercises(generics.RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get(self, request, *args, **kwargs):
        patient = get_patient_from_token(request)
        if isinstance(Patient, patient):
            exercises = Patient.exercise_set.all()
            serializer = ExerciseSerializer(exercises, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "permission denied"})


class PatientSessions(generics.RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get(self, request, *args, **kwargs):
        patient = get_patient_from_token(request)
        if isinstance(Patient, patient):
            sessions = Session.objects.filter(patient=patient)
            serializer = SessionSerializer(sessions, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "permission denied"})


@api_view(["GET", "PATCH", "POST", "DELETE"])
def patient_profile(request):
    patient = get_patient_from_token(request)

    if request.method == "GET":
        serializer = PatientSerializer(patient)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = PatientSerializer(patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_BAD_REQUEST)

    if request.method == "PATCH":
        return Response(
            {"error": "Use POST method to update your profile."},
            status=status.HTTP_METHOD_NOT_ALLOWED,
        )

    if request.method == "DELETE":
        patient.delete()
        return Response(
            {"message": "Profile deleted successfully."}, status=status.HTTP_200_OK
        )

class PatientDoctorView(APIView):
    def get(self, request):
        patient = get_patient_from_token(request)
        if isinstance(patient, Patient):
            doctor = patient.doctor
            serializer = DoctorSerializer(doctor)
            return Response(serializer.data)
        else:
            return Response({"error": "permission denied"})