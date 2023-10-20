# from rest_framework import generics, permissions
# from rest_framework.response import Response
# from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# from .models import Doctor
# from .serializers import DoctorSerializer
# from doctor.permissions import IsDoctorOwnerPermission
# from exercise.serializers import ExerciseSerializer
# from session.serializers import SessionSerializer
# from patient.serializers import PatientSerializer


# class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Doctor.objects.all()
#     serializer_class = DoctorSerializer
#     authentication_classes = [JSONWebTokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated, IsDoctorOwnerPermission]

#     def get(self, request, *args, **kwargs):
#         doctor = self.get_object()
#         if isinstance(doctor, Doctor):
#             serializer = DoctorSerializer(doctor)
#             return Response(serializer.data)
#         else:
#             return Response({"error": "permission denied"})


# class DoctorExercises(generics.RetrieveAPIView):
#     queryset = Doctor.objects.all()
#     serializer_class = DoctorSerializer
#     authentication_classes = [JSONWebTokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated, IsDoctorOwnerPermission]

#     def get(self, request, *args, **kwargs):
#         doctor = self.get_object()
#         if isinstance(doctor, Doctor):
#             exercises = doctor.exercise_set.all()
#             serializer = ExerciseSerializer(exercises, many=True)
#             return Response(serializer.data)
#         else:
#             return Response({"error": "permission denied"})


# class DoctorPatients(generics.RetrieveAPIView):
#     queryset = Doctor.objects.all()
#     serializer_class = DoctorSerializer
#     authentication_classes = [JSONWebTokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated, IsDoctorOwnerPermission]

#     def get(self, request, *args, **kwargs):
#         doctor = self.get_object()
#         if isinstance(doctor, Doctor):
#             patients = doctor.patient_set.all()
#             serializer = PatientSerializer(patients, many=True)
#             return Response(serializer.data)
#         else:
#             return Response({"error": "permission denied"})


# class DoctorSessions(generics.RetrieveAPIView):
#     queryset = Doctor.objects.all()
#     serializer_class = DoctorSerializer
#     authentication_classes = [JSONWebTokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated, IsDoctorOwnerPermission]

#     def get(self, request, *args, **kwargs):
#         doctor = self.get_object()
#         if isinstance(doctor, Doctor):
#             sessions = doctor.session_set.all()
#             serializer = SessionSerializer(sessions, many=True)
#             return Response(serializer.data)
#         else:
#             return Response({"error": "permission denied"})

# views.py in doctor app
from rest_framework import generics
from doctor.models import Doctor, Patient
from doctor.serializers import DoctorSerializer
from rest_framework.permissions import IsAuthenticated


class DoctorListView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]


class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]


# views.py in doctor app
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework_simplejwt.views import TokenObtainPairView


class DoctorLoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        doctors = Doctor.objects.filter(user=user,is_active=True)
        patient = Patient.objects.filter(user=user, is_active=True)
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
