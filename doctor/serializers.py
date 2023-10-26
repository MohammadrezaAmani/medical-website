from rest_framework import serializers
from doctor.models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    """
    Serializer for Doctor model.
    Excludes password field from serialization.
    """
    class Meta:
        model = Doctor
        exclude = ("password",)


class DoctorLoginSerializer(serializers.Serializer):
    """
    Serializer for Doctor login.
    Contains username and password fields.
    """
    username = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)
