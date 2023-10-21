from typing import Any
from rest_framework import serializers
from patient.models import Patient
from django.contrib.auth.models import User


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        exclude = ["user", "password"]


class PatientLoginSerializer(serializers.Serializer):
    username = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)


class PatientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        exclude = ["user"]

    def create(self, validated_data):
        try:
            patient = Patient.objects.create(**validated_data)
            user = User.objects.create_user(
                username=validated_data["username"],
                email=validated_data["email"],
            )
            user.set_password(validated_data["password"])
            patient.user = user
            patient.save()
            user.save()
        except Exception:
            # if user already exists edit it
            user = User.objects.get(username=validated_data["username"])
            user.set_password(validated_data["password"])
            user.email = validated_data["email"]
            user.save()
            patient = Patient.objects.get(user=user)
            patient = super().update(patient, validated_data)
            patient.save()
            user.save()
        return patient

    def update(self, instance: Any, validated_data: Any) -> Any:
        patient = super().update(instance, validated_data)
        user = patient.user
        user.username = validated_data["username"]
        user.email = validated_data["email"]
        user.set_password(validated_data["password"])
        patient.save()
        user.save()
        return patient
