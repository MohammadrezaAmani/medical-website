import jwt
from django.conf import settings
from django.http import JsonResponse
from django.contrib.auth.models import User
from doctor.models import Doctor
from patient.models import Patient

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
