import jwt
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from exercise.serializers import ExerciseSerializer
from patient.serializers import PatientSerializer
from session.serializers import SessionSerializer
from .serializers import DoctorLoginSerializer, DoctorSerializer
from .models import Doctor, Patient


def get_user_from_token(request):
    token = request.META.get("HTTP_AUTHORIZATION")
    if token:
        try:
            token = token.replace("Bearer ", "")
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user_id = payload.get("user_id")
            try:
                user = User.objects.get(id=user_id)
                return user
            except User.DoesNotExist:
                return None
        except jwt.ExpiredSignatureError:
            return JsonResponse({"error": "Token has expired"}, status=401)
        except jwt.DecodeError:
            return JsonResponse({"error": "Invalid token"}, status=401)
    else:
        return JsonResponse({"error": "Token not provided"}, status=401)


def get_doctor_from_token(request):
    try:
        user = get_user_from_token(request)
        doctor = Doctor.objects.get(user=user)
        print(doctor)
        return doctor
    except Doctor.DoesNotExist:
        return None


def get_patient_from_token(request):
    try:
        user = get_user_from_token(request)
        patient = Patient.objects.get(user=user)
        return patient
    except Patient.DoesNotExist:
        return None


class DoctorLoginView(APIView):
    serializer_class = DoctorLoginSerializer

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        print(user)
        doctors = Doctor.objects.filter(user=user, is_active=True, is_doctor=True)
        patient = Patient.objects.filter(user=user, is_active=True, is_doctor=False)
        if len(doctors) > 0:
            if doctors[0].is_active:
                refresh = RefreshToken.for_user(user)
                return Response(
                    {
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                        "user_id": user.id,
                        "is_doctor": True,
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
                        "is_doctor": False,
                    }
                )
        else:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )


class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def get(self, request, *args, **kwargs):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor):
            serializer = DoctorSerializer(doctor)
            return Response(serializer.data)
        else:
            return Response({"error": "permission denied"})


class DoctorExercises(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def get(self, request, *args, **kwargs):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor):
            exercises = doctor.exercise_set.all()
            serializer = ExerciseSerializer(exercises, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "permission denied"})


class DoctorPatients(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def get(self, request, *args, **kwargs):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor):
            patients = doctor.patient_set.all()
            serializer = PatientSerializer(patients, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "permission denied"})


class DoctorSessions(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def get(self, request, *args, **kwargs):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor):
            sessions = doctor.session_set.all()
            serializer = SessionSerializer(sessions, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "permission denied"})


class DoctorMe(APIView):
    seializer_class = DoctorSerializer

    def get(self, request):
        doctor = get_doctor_from_token(request)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)
