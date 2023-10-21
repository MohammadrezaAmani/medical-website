from rest_framework import serializers
from patient.models import Patient
from django.contrib.auth.models import User


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"


class PatientLoginSerializer(serializers.Serializer):
    username = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)


class PatientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = "__all__"
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {"write_only": True},
        }

    def create(self, validated_data):
        patient = Patient.objects.create(**validated_data)
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        patient.user = user
        user.save()
        patient.save()
        return patient