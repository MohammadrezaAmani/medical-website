import jwt
from django.conf import settings
from django.http import Http404, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
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
from .serializers import DoctorLoginSerializer, DoctorSerializer
from .models import Doctor


def get_user_from_token(request):
    token = request.headers.get("Authorization")
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
        if isinstance(user, User):
            doctor = Doctor.objects.get(user=user)
            print(doctor)
            return doctor
        else:
            return user
    except Doctor.DoesNotExist:
        return None


def get_patient_from_token(request):
    try:
        user = get_user_from_token(request)
        if isinstance(user, User):
            patient = Patient.objects.get(user=user)
            return patient
        else:
            return user
    except Patient.DoesNotExist:
        return None


class DoctorLoginView(APIView):
    serializer_class = DoctorLoginSerializer
    pagination_class = PageNumberPagination

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
            status=status.HTTP_METHOD_NOT_ALLOWED,
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
            sessions = Session.objects.filter(patient__doctor=doctor)
            serializer = SessionSerializer(sessions, many=True)
            return Response(serializer.data)
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
            session = Session.objects.get(id=kwargs["pk"])
            session.delete()
            return Response(
                {"message": "Session deleted successfully."}, status=status.HTTP_200_OK
            )
        else:
            return Response({"error": "permission denied"})

    def get_object(self, request, *args, **kwargs):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor) is False:
            return doctor
        if isinstance(doctor, Doctor):
            try:
                return Session.objects.get(pk=kwargs["pk"])
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
            exercise = Exercise.objects.filter(patient__doctor=doctor)
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
            exercise = Exercise.objects.filter(patient__doctor=doctor)
            serializer = ExerciseSerializer(exercise, many=True)
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
            exercise = Exercise.objects.get(id=kwargs["pk"])
            exercise.delete()
            return Response(
                {"message": "exercise deleted successfully."}, status=status.HTTP_200_OK
            )
        else:
            return Response({"error": "permission denied"})

    def get_object(self, request, *args, **kwargs):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor) is False:
            return doctor
        if isinstance(doctor, Doctor):
            try:
                return Exercise.objects.get(pk=kwargs["pk"])
            except Exercise.DoesNotExist:
                raise Http404
        else:
            return Response({"error": "permission denied"})


class AddPatient(APIView):
    serializer_class = PatientCreateSerializer

    def post(self, request):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor):
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
            serializer = ExerciseSerializer(data=request.data)
            if serializer.is_valid():
                serializer.owner = doctor
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
            sessions = Session.objects.filter(patient__doctor=doctor, date=kwargs["date"])
            serializer = SessionSerializer(sessions, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "permission denied"})