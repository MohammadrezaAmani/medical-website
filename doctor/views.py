from django.http import Http404
from django.contrib.auth import authenticate
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.tokens import RefreshToken
from exercise.serializers import ExerciseSerializer, ExerciseCreateSerializer
from exercise.models import Exercise
from patient.serializers import PatientSerializer, PatientCreateSerializer
from patient.models import Patient
from session.serializers import SessionSerializer
from session.models import Session
from utils.auth import (
    get_doctor_from_token,
)
from .serializers import DoctorLoginSerializer, DoctorSerializer
from .models import Doctor


class DoctorLoginView(APIView):
    serializer_class = DoctorLoginSerializer
    pagination_class = PageNumberPagination

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        doctors = Doctor.objects.filter(user=user)
        patient = Patient.objects.filter(user=user)
        if len(doctors) > 0:
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


@api_view(["GET", "PATCH", "POST", "DELETE"])
def doctor_profile(request):
    doctor = get_doctor_from_token(request)
    if isinstance(doctor, Doctor) is False:
        return doctor

    if request.method == "GET":
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = DoctorSerializer(doctor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PATCH":
        return Response(
            {"error": "Use POST method to update your profile."},
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )

    if request.method == "DELETE":
        doctor.delete()
        return Response(
            {"message": "Profile deleted successfully."}, status=status.HTTP_200_OK
        )


class DoctorPatients(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor) is False:
            return doctor
        if isinstance(doctor, Doctor):
            patients = doctor.patients.all()
            serializer = PatientSerializer(patients, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "permission denied"})




class DoctorPatientDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor) is False:
            return doctor
        if isinstance(doctor, Doctor):
            try:
                sessions = Patient.objects.filter(
                    patient__doctor=doctor, id=kwargs["pk"]
                )
                sessions = sessions[0]
                serializer = PatientSerializer(sessions)
                return Response(serializer.data)
            except Patient.DoesNotExist:
                raise Http404
        else:
            return Response({"error": "permission denied"})

    def patch(self, request, *args, **kwargs):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor) is False:
            return doctor
        if isinstance(doctor, Doctor):
            session = Patient.objects.get(id=kwargs["pk"])
            serializer = PatientSerializer(session, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "permission denied"})

    def delete(self, request, *args, **kwargs):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor) is False:
            return doctor
        if isinstance(doctor, Doctor):
            try:
                session = Patient.objects.get(id=kwargs["pk"])
                session.delete()
                return Response(
                    {"message": "Patient deleted successfully."},
                    status=status.HTTP_200_OK,
                )
            except Patient.DoesNotExist:
                raise Http404
        else:
            return Response({"error": "permission denied"})


class DoctorMe(APIView):
    seializer_class = DoctorSerializer

    def get(self, request):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor) is False:
            return doctor
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)


class AddSession(APIView):
    serializer_class = SessionSerializer

    def post(self, request):
        doctor = get_doctor_from_token(request)
        print(request.data)
        if isinstance(doctor, Doctor) is False:
            return doctor
        if isinstance(doctor, Doctor):
            serializer = SessionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "permission denied"})


class DoctorSessions(generics.RetrieveAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor) is False:
            return doctor
        if isinstance(doctor, Doctor):
            sessions = Session.objects.filter(patient__doctor=doctor)
            serializer = SessionSerializer(sessions, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "permission denied"})


class DoctorSessionsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor) is False:
            return doctor
        if isinstance(doctor, Doctor):
            try:
                sessions = Session.objects.filter(
                    patient__doctor=doctor, id=kwargs["pk"]
                )
                sessions = sessions[0]
                serializer = SessionSerializer(sessions)
                return Response(serializer.data)
            except Session.DoesNotExist:
                raise Http404
        else:
            return Response({"error": "permission denied"})

    def patch(self, request, *args, **kwargs):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor) is False:
            return doctor
        if isinstance(doctor, Doctor):
            session = Session.objects.get(id=kwargs["pk"])
            serializer = SessionSerializer(session, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "permission denied"})

    def delete(self, request, *args, **kwargs):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor) is False:
            return doctor
        if isinstance(doctor, Doctor):
            try:
                session = Session.objects.get(id=kwargs["pk"])
                session.delete()
                return Response(
                    {"message": "Session deleted successfully."},
                    status=status.HTTP_200_OK,
                )
            except Session.DoesNotExist:
                raise Http404
        else:
            return Response({"error": "permission denied"})


class DoctorExercises(generics.RetrieveAPIView):
    pagination_class = PageNumberPagination
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def get(self, request, *args, **kwargs):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor) is False:
            return doctor
        if isinstance(doctor, Doctor):
            exercise = Exercise.objects.filter(owner=doctor)
            serializer = ExerciseSerializer(exercise, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "permission denied"})


class DoctorExerciseDetails(generics.RetrieveUpdateDestroyAPIView):
    pagination_class = PageNumberPagination
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def get(self, request, *args, **kwargs):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor) is False:
            return doctor
        if isinstance(doctor, Doctor):
            exercise = Exercise.objects.filter(owner=doctor, id=kwargs["pk"])
            if len(exercise) == 0:
                return Response({"error": "permission denied"})
            exercise = exercise[0]
            serializer = ExerciseSerializer(exercise)
            return Response(serializer.data)
        else:
            return Response({"error": "permission denied"})

    def patch(self, request, *args, **kwargs):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor) is False:
            return doctor
        if isinstance(doctor, Doctor):
            exercise = Exercise.objects.get(id=kwargs["pk"])
            serializer = ExerciseSerializer(exercise, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "permission denied"})

    def delete(self, request, *args, **kwargs):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor) is False:
            return doctor
        if isinstance(doctor, Doctor):
            try:
                exercise = Exercise.objects.get(id=kwargs["pk"])
                exercise.delete()

                return Response(
                    {"message": "exercise deleted successfully."},
                    status=status.HTTP_200_OK,
                )
            except Exercise.DoesNotExist:
                raise Http404
        else:
            return Response({"error": "permission denied"})


class AddPatient(APIView):
    serializer_class = PatientCreateSerializer

    def post(self, request):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor):
            request.data["doctor"] = doctor.id
            serializer = PatientCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "permission denied"})


class AddExercise(APIView):
    serializer_class = ExerciseCreateSerializer

    def post(self, request):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor):
            request.data["owner"] = doctor.id
            serializer = ExerciseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "permission denied"})


class SessionDate(APIView):
    serializer_class = SessionSerializer

    def get(self, request, *args, **kwargs):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor):
            sessions = Session.objects.filter(
                patient__doctor=doctor, date=kwargs["date"]
            )
            serializer = SessionSerializer(sessions, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "permission denied"})
