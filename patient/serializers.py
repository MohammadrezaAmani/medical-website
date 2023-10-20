from rest_framework import serializers
from patient.models import Patient


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class PatientLoginSerializer(serializers.Serializer):
    username = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)
