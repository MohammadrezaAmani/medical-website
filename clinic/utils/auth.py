import jwt
from django.conf import settings
from django.contrib.auth.models import User
from django.http import JsonResponse
from doctor.models import Doctor
from patient.models import Patient


def get_user_from_token(request):
    """
    Given a request object, extracts the JWT token from the Authorization header,
    decodes it using the app's secret key, and returns the corresponding User object.

    If the token is invalid or has expired, returns an appropriate error response.

    Args:
        request: HttpRequest object representing the incoming request.

    Returns:
        User object corresponding to the user ID stored in the JWT token, or None if the token is invalid.
    """
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
    """
    Returns the doctor object associated with the given request's token.

    Args:
        request (HttpRequest): The request object containing the token.

    Returns:
        Doctor: The doctor object associated with the token, or None if not found.
    """
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
    """
    Given a request object, retrieves the patient associated with the user token in the request.
    If the user is not a patient, returns the user object instead.
    If the patient does not exist, returns None.
    """
    try:
        user = get_user_from_token(request)
        if isinstance(user, User):
            patient = Patient.objects.get(user=user)
            return patient
        else:
            return None
    except Patient.DoesNotExist:
        return None
