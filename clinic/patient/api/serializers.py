from typing import Any

from django.contrib.auth.models import User
from patient.models import Patient
from prescription.models import Prescription
from rest_framework import serializers
from session.models import Session

from clinic.exercise.api.serializers import ExerciseSerializer

from ..utils import random_password_generator


class PatientSerializer(serializers.ModelSerializer):
    """
    Serializer for the Patient model.
    """

    class Meta:
        model = Patient
        exclude = ["user"]
        print("hi")

        #    def update(self, instance: Any, validated_data: Any) -> Any:
        """
        Update the patient instance with the validated data.

        Args:
            instance (Any): The patient instance to update.
            validated_data (Any): The validated data to update the instance with.

        Returns:
            Any: The updated patient instance.
        """
        # print(instance.id)


#       patient = Patient.objects.filter(id=instance.id)

#      print(type(patient))
# user = patient.user
# if "email" in validated_data:
#   user.email = validated_data["email"]
#     patient.save()
# user.save()
#    return patient


class PatientLoginSerializer(serializers.Serializer):
    """
    Serializer for patient login.

    Fields:
    - username: EmailField with max length of 100 characters.
    - password: CharField with max length of 100 characters.
    """

    username = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)


class PatientCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and updating Patient instances.

    Excludes 'user' and 'id' fields from the serialized data.
    Generates a random password for the patient and creates a user instance with the patient's phone number as the username.
    """

    class Meta:
        model = Patient
        exclude = ["user", "id"]

    def create(self, validated_data):
        """
        Creates a new Patient instance with the given validated data.

        Generates a random password for the patient and creates a user instance with the patient's phone number as the username.

        Args:
            validated_data: The validated data to create the patient instance with.

        Returns:
            The created patient instance.
        """
        print(validated_data["phone_number"])
        try:
            if Patient.objects.filter(
                phone_number=validated_data["phone_number"]
            ).exists():
                return {"error": "Patient with this phone number already exists"}
            print("USER CREATED")
            patient = Patient.objects.create(**validated_data)
            username = patient.phone_number
            password = random_password_generator()
            patient.password = password
            user = User.objects.create_user(
                username=username,
                email=validated_data["email"],
            )
            user.set_password(password)
            patient.user = user
            patient.save()
            user.save()
            return patient
        except Exception as e:
            return {"error": str(e)}

    def update(self, instance: Any, validated_data: Any) -> Any:
        """
        Updates an existing Patient instance with the given validated data.

        Updates the patient's email and saves the changes to the patient and user instances.

        Args:
            instance: The existing patient instance to update.
            validated_data: The validated data to update the patient instance with.

        Returns:
            The updated patient instance.
        """
        try:
            patient = super().update(instance, validated_data)
            user = patient.user
            user.email = validated_data["email"]
            patient.save()
            user.save()
            return patient
        except Exception as e:
            return {"error": str(e)}


# In your patient/serializers.py
class PrescriptionSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = Prescription
        fields = [
            "id",
            "exercises",
            "repeat",
            "sets",
            "hold_time",
            "total_time",
            "rest_time",
        ]


class SessionSerializer(serializers.ModelSerializer):
    prescriptions = PrescriptionSerializer(many=True, read_only=True)

    class Meta:
        model = Session
        fields = [
            "id",
            "patient",
            "prescriptions",
            "date",
            "time",
            "session_type",
            "status",
            "rate",
            "description",
        ]
