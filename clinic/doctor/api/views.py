from django.contrib.auth import authenticate
from django.http import Http404
from exercise.models import Exercise
from clinic.exercise.api.serializers import ExerciseCreateSerializer, ExerciseSerializer
from patient.models import Patient
from clinic.patient.api.serializers import PatientCreateSerializer, PatientSerializer
from prescription.models import Prescription
from clinic.prescription.api.serializers import PrescriptionSerializer
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from session.models import Session
from clinic.session.api.serializers import SessionSerializer
from utils.auth import get_doctor_from_token

from ..models import Doctor
from .serializers import DoctorLoginSerializer, DoctorSerializer


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
    """
    API endpoint that allows a doctor to retrieve, update or delete a patient's details.
    """

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        """
        Retrieve a patient's details.
        """
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

    def put(self, request, pk):
        """
        Update a patient's details.
        """
        doctor = get_doctor_from_token(request)
        if not isinstance(doctor, Doctor):
            return doctor
        session = Patient.objects.get(id=pk)
        serializer = PatientSerializer(session, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a patient's details.
        """
        doctor = get_doctor_from_token(request)
        if not isinstance(doctor, Doctor):
            return doctor
        try:
            session = Patient.objects.get(id=pk)
            session.delete()
            return Response(
                {"message": "Patient deleted successfully."},
                status=status.HTTP_200_OK,
            )
        except Patient.DoesNotExist:
            raise Http404


class DoctorMe(generics.RetrieveAPIView):
    """
    API endpoint that allows a doctor to retrieve their own details.
    """

    serializer_class = DoctorSerializer

    def get(self, request):
        """
        Retrieve a doctor's own details.
        """
        doctor = get_doctor_from_token(request)
        if not isinstance(doctor, Doctor):
            return doctor
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)


class AddSession(generics.RetrieveAPIView):
    """
    API endpoint that allows a doctor to add a session.
    """

    serializer_class = SessionSerializer

    def post(self, request):
        """
        Add a session.
        """
        doctor = get_doctor_from_token(request)
        if not isinstance(doctor, Doctor):
            return doctor
        serializer = SessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DoctorSessions(generics.RetrieveAPIView):
    """
    API endpoint that allows a doctor to retrieve their own sessions.
    """

    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    pagination_class = PageNumberPagination

    def get(self, request, *args, **kwargs):
        """
        Retrieve a doctor's own sessions.
        """
        doctor = get_doctor_from_token(request)
        if not isinstance(doctor, Doctor):
            return doctor
        sessions = Session.objects.filter(patient__doctor=doctor)
        serializer = SessionSerializer(sessions, many=True)
        return Response(serializer.data)


class DoctorSessionsDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a doctor to retrieve, update or delete a session.
    """

    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    pagination_class = PageNumberPagination

    def get(self, request, pk):
        """
        Retrieve a session.
        """
        doctor = get_doctor_from_token(request)
        if not isinstance(doctor, Doctor):
            return doctor
        try:
            sessions = Session.objects.filter(patient__doctor=doctor, id=pk)
            sessions = sessions[0]
            serializer = SessionSerializer(sessions)
            return Response(serializer.data)
        except Session.DoesNotExist:
            raise Http404

    def patch(self, request, pk):
        """
        Update a session.
        """
        doctor = get_doctor_from_token(request)
        if not isinstance(doctor, Doctor):
            return doctor
        session = Session.objects.get(id=pk)
        serializer = SessionSerializer(session, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Delete a session.
        """
        doctor = get_doctor_from_token(request)
        if not isinstance(doctor, Doctor):
            return doctor
        try:
            session = Session.objects.get(id=pk)
            session.delete()
            return Response(
                {"message": "Session deleted successfully."},
                status=status.HTTP_200_OK,
            )
        except Session.DoesNotExist:
            raise Http404


class DoctorExercises(generics.RetrieveAPIView):
    pagination_class = PageNumberPagination
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def get(self, request):
        doctor = get_doctor_from_token(request)
        if not isinstance(doctor, Doctor):
            return doctor
        exercise = Exercise.objects.filter(owner=doctor)
        serializer = ExerciseSerializer(exercise, many=True)
        return Response(serializer.data)


class DoctorExerciseDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a doctor to retrieve, update, or delete an exercise.

    get:
    Retrieve an exercise instance.

    patch:
    Update an exercise instance.

    delete:
    Delete an exercise instance.
    """

    pagination_class = PageNumberPagination
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def get(self, request, *args, **kwargs):
        """
        Retrieve an exercise instance.

        Args:
            request: The HTTP request.
            args: Additional arguments.
            kwargs: Additional keyword arguments.

        Returns:
            A Response object containing the serialized exercise instance.
        """
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
        """
        Update an exercise instance.

        Args:
            request: The HTTP request.
            args: Additional arguments.
            kwargs: Additional keyword arguments.

        Returns:
            A Response object containing the serialized exercise instance if the update is successful,
            or a Response object containing the errors if the update is unsuccessful.
        """
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
        """
        Delete an exercise instance.

        Args:
            request: The HTTP request.
            args: Additional arguments.
            kwargs: Additional keyword arguments.

        Returns:
            A Response object containing a success message if the deletion is successful,
            or a Http404 exception if the exercise instance does not exist.
        """
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


class AddPatient(generics.CreateAPIView):
    serializer_class = PatientSerializer

    def post(self, request):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor):
            request.data["doctor"] = doctor.id
            serializer = PatientCreateSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                patient = Patient.objects.get(
                    phone_number=serializer.data["phone_number"]
                )
                print(patient, "-----------------------")
                return Response(PatientSerializer(patient).data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "permission denied"})


class AddExercise(generics.CreateAPIView):
    """
    API endpoint to add a new exercise for a doctor.

    Methods:
    --------
    post(request):
        Add a new exercise for the authenticated doctor.

    Attributes:
    -----------
    serializer_class: ExerciseCreateSerializer
        Serializer class for creating a new exercise.
    """

    serializer_class = ExerciseCreateSerializer

    def post(self, request):
        """
        Add a new exercise for the authenticated doctor.

        Parameters:
        -----------
        request: Request
            HTTP request object.

        Returns:
        --------
        Response:
            HTTP response object.
        """
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


class SessionDate(generics.RetrieveAPIView):
    """
    API endpoint that returns all sessions for a specific date for a doctor's patients.

    Args:
        request (HttpRequest): The HTTP request object.
        date (str): The date for which sessions are to be retrieved.

    Returns:
        Response: A JSON response containing the serialized session data.
    """

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


class AddPrescription(generics.CreateAPIView):
    serializer_class = PrescriptionSerializer

    def post(self, request):
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor):
            serializer = PrescriptionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "permission denied"})


class DoctorPrescriptionDetails(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that allows a doctor to retrieve, update, or delete an Prescription.

    get:
    Retrieve an Prescription instance.

    patch:
    Update an Prescription instance.

    delete:
    Delete an Prescription instance.
    """

    pagination_class = PageNumberPagination
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

    def get(self, request, *args, **kwargs):
        """
        Retrieve an prescription instance.

        Args:
            request: The HTTP request.
            args: Additional arguments.
            kwargs: Additional keyword arguments.

        Returns:
            A Response object containing the serialized prescription instance.
        """
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor) is False:
            return doctor
        if isinstance(doctor, Doctor):
            prescription = Prescription.objects.filter(owner=doctor, id=kwargs["pk"])
            if len(prescription) == 0:
                return Response({"error": "permission denied"})
            prescription = prescription[0]
            serializer = PrescriptionSerializer(prescription)
            return Response(serializer.data)
        else:
            return Response({"error": "permission denied"})

    def patch(self, request, *args, **kwargs):
        """
        Update an Prescription instance.

        Args:
            request: The HTTP request.
            args: Additional arguments.
            kwargs: Additional keyword arguments.

        Returns:
            A Response object containing the serialized Prescription instance if the update is successful,
            or a Response object containing the errors if the update is unsuccessful.
        """
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor) is False:
            return doctor
        if isinstance(doctor, Doctor):
            prescription = Prescription.objects.get(id=kwargs["pk"])
            serializer = PrescriptionSerializer(
                prescription, data=request.data, partial=True
            )
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "permission denied"})

    def delete(self, request, *args, **kwargs):
        """
        Delete an Prescription instance.

        Args:
            request: The HTTP request.
            args: Additional arguments.
            kwargs: Additional keyword arguments.

        Returns:
            A Response object containing a success message if the deletion is successful,
            or a Http404 exception if the Prescription instance does not exist.
        """
        doctor = get_doctor_from_token(request)
        if isinstance(doctor, Doctor) is False:
            return doctor
        if isinstance(doctor, Doctor):
            try:
                prescription = Prescription.objects.get(id=kwargs["pk"])
                prescription.delete()

                return Response(
                    {"message": "prescription deleted successfully."},
                    status=status.HTTP_200_OK,
                )
            except Prescription.DoesNotExist:
                raise Http404
        else:
            return Response({"error": "permission denied"})
