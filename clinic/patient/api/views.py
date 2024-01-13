from datetime import datetime

from django.contrib.auth import authenticate
from doctor.models import Doctor
from clinic.doctor.api.serializers import DoctorSerializer
from exercise.models import Equipment
from clinic.exercise.api.serializers import ExerciseSerializer
from patient.models import Patient
from clinic.patient.api.serializers import PatientLoginSerializer, PatientSerializer
from clinic.prescription.api.serializers import PrescriptionSerializer
from reports.models import PrescriptionReport
from clinic.reports.api.serializers import (
    PrescriptionReportExtendedSerializer,
    PrescriptionReportSerializer,
)
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from session.models import Session
from clinic.session.api.serializers import SessionSerializer
from utils.auth import get_patient_from_token


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
        # login(request, user)
        #        doctor = Patient.objects.filter(user=user, is_active=True, is_patient=True)
        #       patient = Patient.objects.filter(user=user, is_active=True, is_patient=False)
        if not user:
            return Response("wrong_password", status=status.HTTP_403_FORBIDDEN)
        #  doctor =  Poctor.objects.filter(user=user)
        patient = Patient.objects.filter(user=user)
        serializer = PatientSerializer(patient[0])
        print(serializer.data)
        # if len(doctor) > 0:
        #          if doctor[0].is_active:
        # refresh = RefreshToken.for_user(user)
        # return Response(
        #      {
        #           "refresh": str(refresh),
        #            "access": str(refresh.access_token),
        #             "user_id": user.id,g
        #              "is_patient": True,
        #           }
        #        )
        if len(patient) > 0:
            #         if patient[0].is_active:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "user_id": user.id,
                    "is_patient": True,
                    "profile_img": serializer.data["photo"],
                    "name": str(patient[0]),
                    "support_phone_number": "+989154971975",
                    "support_mail": "amirmasoud.sepehrian@gmail.com",
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
        if patient:
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
    if isinstance(patient, Patient):
        if request.method == "GET":
            serializer = PatientSerializer(patient)
            return Response(serializer.data)

        if request.method == "POST":
            serializer = PatientSerializer(patient, data=request.data, partial=True)
            print(serializer)
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
            patient.delete()
            return Response(
                {"message": "Profile deleted successfully."}, status=status.HTTP_200_OK
            )
    else:
        return Response(
            {"message": "permission deny."}, status=status.HTTP_403_FORBIDDEN
        )


class PatientDoctorView(generics.RetrieveAPIView):
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


class PatientSessions2(generics.ListAPIView):
    """
    API endpoint that returns all sessions for a specific date for a patient.

    Args:
        request (HttpRequest): The HTTP request object.
        date (str): The date for which sessions are to be retrieved.

    Returns:
        Response: A JSON response containing the serialized session data.
    """

    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def get(self, request, *args, **kwargs):
        patient = get_patient_from_token(request)
        if isinstance(patient, Patient):
            # Get start and end date from the GET request parameters
            start_date_str = request.GET.get("start_date", None)
            end_date_str = request.GET.get("end_date", None)

            if start_date_str and end_date_str:
                try:
                    # Convert start and end date strings to datetime objects
                    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
                    end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

                    # Filter sessions within the specified time period
                    sessions = Session.objects.filter(
                        patient=patient, date__range=[start_date, end_date]
                    )
                    serializer = SessionSerializer(sessions, many=True)
                    return Response(serializer.data)
                except ValueError:
                    return Response(
                        {"error": "Invalid date format. Use 'YYYY-MM-DD'."}, status=400
                    )
            else:
                return Response(
                    {
                        "error": "Both start_date and end_date are required in the GET request."
                    },
                    status=400,
                )
        else:
            return Response({"error": "Permission denied"}, status=403)


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def patient_session_exercises(request, session_id):
    """
    API view for retrieving exercises for all prescriptions in a specific session for a patient.

    This view requires a valid patient token to be included in the request headers.
    If the token is valid and belongs to the patient, it retrieves the session and returns
    a JSON containing all prescriptions and their associated exercises.

    Args:
        request (HttpRequest): The HTTP request object.
        session_id (int): The ID of the session for which exercises are to be retrieved.

    Returns:
        Response: A JSON response containing the serialized prescription and exercise data.
    """
    patient = get_patient_from_token(request)

    if not patient:
        return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        # Retrieve the session for the given session_id
        session = Session.objects.get(id=session_id, patient=patient)

        # Get all prescriptions associated with the session
        prescriptions = session.prescription.all()

        # Serialize prescriptions along with their associated exercises
        prescription_data = []
        for prescription in prescriptions:
            serializer = PrescriptionSerializer(prescription)
            prescription_data.append(
                {
                    "prescription": serializer.data,
                    #   "exercises": exercises_serializer.data,
                }
            )

        return Response(prescription_data)
    except Session.DoesNotExist:
        return Response(
            {"error": "Session not found"}, status=status.HTTP_404_NOT_FOUND
        )
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def session_details(request, session_id):
    patient = get_patient_from_token(request)

    if not patient:
        return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)

    try:
        session = Session.objects.get(pk=session_id, patient=patient)
        serializer = SessionSerializer(session)

        # Calculate total time of each session
        total_time = 0
        for prescription in serializer.data["prescription"]:
            total_time += prescription["total_time"]

        # Get all unique accessories for a session
        all_accessories = set()
        for prescription in serializer.data["prescription"]:
            for exercise in prescription["exercises"]:
                accessories = exercise["accessories"]
                all_accessories.update(accessories)

        return Response(
            {
                "total_time": total_time,
                "all_accessories": list(all_accessories),
                "session_details": serializer.data,
            }
        )
    except Session.DoesNotExist:
        return Response({"error": "Session does not exist"}, status=404)


@api_view(["POST"])
##@permission_classes([IsAuthenticated])
def create_prescription_report(request, session_id):
    patient = get_patient_from_token(request)

    if not patient:
        return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        session = Session.objects.get(pk=session_id)
    except Session.DoesNotExist:
        return Response(
            {"error": "Session does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    if request.method == "POST":
        report_data = request.data
        repeats = []
        for prescription_id, values in report_data.items():
            try:
                prescription = session.prescription.get(pk=prescription_id)
            except prescription.DoesNotExist:
                return Response(
                    {"error": f"Prescription with ID {prescription_id} does not exist"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            serializer = PrescriptionReportSerializer(data=values)
            repeats.append(values["repeats"])
            if serializer.is_valid():
                serializer.save(session=session, prescription=prescription)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        session.status = "c"
        sum = 0
        for rep in repeats:
            sum += rep
        session.rate = (sum / len(repeats)) * 100
        session.save()
        return Response(
            {"message": "Reports submitted successfully"}, status=status.HTTP_200_OK
        )


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def get_session_reports_with_detail(request, session_id):
    patient = get_patient_from_token(request)

    if not patient:
        return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        session = Session.objects.get(pk=session_id)
    except Session.DoesNotExist:
        return Response(
            {"error": "Session does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    reports = PrescriptionReport.objects.filter(session=session)
    serializer = PrescriptionReportExtendedSerializer(reports, many=True)
    return Response(serializer.data)


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def get_session_reports(request, session_id):
    patient = get_patient_from_token(request)

    if not patient:
        return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
    try:
        session = Session.objects.get(pk=session_id)
    except Session.DoesNotExist:
        return Response(
            {"error": "Session does not exist"}, status=status.HTTP_404_NOT_FOUND
        )
    reports = PrescriptionReport.objects.filter(session=session)
    serializer = PrescriptionReportSerializer(reports, many=True)
    return Response(serializer.data)


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def get_last_k_sessions_reports(request, k):
    patient = get_patient_from_token(request)

    if not patient:
        return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
    if not str(k).isdigit() or int(k) <= 0:
        return Response(
            {"error": "Invalid value for 'k'"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        patient = get_patient_from_token(request)
        sessions = Session.objects.filter(patient=patient).order_by("-date", "-time")[
            : int(k)
        ]
    except Patient.DoesNotExist:
        return Response(
            {"error": "Patient does not exist"}, status=status.HTTP_404_NOT_FOUND
        )

    reports = PrescriptionReport.objects.filter(session__in=sessions)
    serializer = PrescriptionReportSerializer(reports, many=True)
    return Response(serializer.data)


@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def combined_session_details(request):
    patient = get_patient_from_token(request)
    print(patient)
    if not patient:
        return Response({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)

    # Get start and end date from the GET request parameters
    start_date_str = request.GET.get("start_date", None)
    end_date_str = request.GET.get("end_date", None)

    if start_date_str and end_date_str:
        try:
            # Convert start and end date strings to datetime objects
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.strptime(end_date_str, "%Y-%m-%d")

            # Filter sessions within the specified time period
            sessions = Session.objects.filter(
                patient=patient, date__range=[start_date, end_date]
            )

            # Serialize sessions with more detail
            serialized_sessions = []
            for session in sessions:
                serializer = SessionSerializer(session)

                total_time = 0
                for prescription in serializer.data["prescription"]:
                    total_time += prescription["total_time"]

                # Get all unique accessories for a session

                all_accessories = []
                all_designer = []
                for prescription in serializer.data["prescription"]:
                    for exercise in prescription["exercises"]:
                        accessories = exercise["accessories"]
                        owner = str(Doctor.objects.get(id=exercise["owner"]))
                        exercise["accessories"] = []
                        if owner not in all_designer:
                            all_designer.append(owner)
                        for _id in accessories:
                            asset = str(Equipment.objects.get(id=_id))
                            if asset not in all_accessories:
                                all_accessories.append(asset)
                                exercise["accessories"].append(asset)

                # Append detailed session data to the list
                serialized_sessions.append(
                    {
                        "owner": all_designer[0] if all_designer else None,
                        "total_time": total_time,
                        "all_accessories": ", ".join(map(str, all_accessories))
                        if all_accessories
                        else None,
                        "session_details": serializer.data,
                    }
                )

            return Response(serialized_sessions)

        except ValueError:
            return Response(
                {"error": "Invalid date format. Use 'YYYY-MM-DD'."}, status=400
            )
    else:
        return Response(
            {"error": "Both start_date and end_date are required in the GET request."},
            status=400,
        )
