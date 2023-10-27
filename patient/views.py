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

from utils.auth import (
    get_patient_from_token,
)


class PatientLoginView(APIView):
    """
    API view for patient login.

    This view handles the POST request for patient login. It authenticates the user
    based on the provided username and password, and returns a response containing
    a refresh token, an access token, the user ID, and a flag indicating whether the
    user is a patient or a doctor. If the credentials are invalid, it returns a 401
    Unauthorized response.
    """

    serializer_class = PatientLoginSerializer

    def post(self, request):
        """
        Handle POST request for patient login.
        """
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        doctor = Patient.objects.filter(user=user, is_active=True, is_patient=True)
        patient = Patient.objects.filter(user=user, is_active=True, is_patient=False)
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
    """
    API view for patient detail.

    This view provides the following HTTP methods:
        - GET: Retrieve patient detail.
        - PATCH: Update patient detail.
        - DELETE: Delete patient detail.

    The view requires a valid token for authentication. If the token is invalid or does not belong to a patient,
    the view returns a "permission denied" error.

    Attributes:
        queryset: Queryset of all Patient objects.
        serializer_class: Serializer class for Patient objects.
    """

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get(self, request, *args, **kwargs):
        """
        Handle GET request for patient detail.
        """
        patient = get_patient_from_token(request)
        if isinstance(patient, Patient):
            serializer = PatientSerializer(patient)
            return Response(serializer.data)
        else:
            return Response({"error": "permission denied"})

    def get_object(self):
        """
        Get patient object.
        """
        patient = get_patient_from_token(self.request)
        if isinstance(patient, Patient):
            serializer = PatientSerializer(patient)
            return Response(serializer.data)
        else:
            return Response({"error": "permission denied"})

    def delete(self, request, *args, **kwargs):
        """
        Handle DELETE request for patient detail.
        """
        patient = get_patient_from_token(request)
        if isinstance(patient, Patient):
            patient.delete()
            return Response({"message": "Patient deleted"})
        else:
            return Response({"error": "permission denied"})

    def patch(self, request, *args, **kwargs):
        """
        Handle PATCH request for patient detail.
        """
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
    """
    API view for retrieving exercises for a patient.

    This view requires a valid patient token to be included in the request headers.
    If the token is valid and belongs to the patient, a list of exercises associated
    with the patient will be returned in the response. Otherwise, a "permission denied"
    error message will be returned.

    Attributes:
        queryset (QuerySet): A QuerySet of all Patient objects.
        serializer_class (Serializer): The serializer class to use for Patient objects.
    """

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get(self, request, *args, **kwargs):
        """
        Handle GET request for patient exercises.
        """
        patient = get_patient_from_token(request)
        if isinstance(Patient, patient):
            exercises = Patient.exercise_set.all()
            serializer = ExerciseSerializer(exercises, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "permission denied"})


class PatientSessions(generics.RetrieveAPIView):
    """
    API view for retrieving patient sessions.

    This view handles GET requests for patient sessions. It retrieves the patient object from the request token,
    and returns a list of sessions associated with that patient. If the patient is not authorized to access the sessions,
    it returns an error message.

    Attributes:
        queryset: A queryset of all Patient objects.
        serializer_class: The serializer class used to serialize Patient objects.
    """

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def get(self, request, *args, **kwargs):
        """
        Handle GET request for patient sessions.
        """
        patient = get_patient_from_token(request)
        if isinstance(Patient, patient):
            sessions = Session.objects.filter(patient=patient)
            serializer = SessionSerializer(sessions, many=True)
            return Response(serializer.data)
        else:
            return Response({"error": "permission denied"})


@api_view(["GET", "PATCH", "POST", "DELETE"])
def patient_profile(request):
    """
    API view for patient profile.

    Methods:
    GET -- Retrieve patient profile.
    POST -- Update patient profile.
    PATCH -- Method not allowed. Use POST method to update your profile.
    DELETE -- Delete patient profile.

    Returns:
    GET -- Patient profile data.
    POST -- Updated patient profile data.
    DELETE -- Success message.

    """
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
    """
    A view to retrieve the doctor associated with a patient.

    Returns the serialized doctor object if the patient is authorized,
    otherwise returns an error message.
    """

    def get(self, request):
        patient = get_patient_from_token(request)
        if isinstance(patient, Patient):
            doctor = patient.doctor
            serializer = DoctorSerializer(doctor)
            return Response(serializer.data)
        else:
            return Response({"error": "permission denied"})
