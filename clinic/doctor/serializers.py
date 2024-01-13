from doctor.models import Doctor
from rest_framework import serializers


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        exclude = ("password",)


class DoctorLoginSerializer(serializers.Serializer):
    username = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)
