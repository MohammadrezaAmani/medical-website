from typing import Any
from rest_framework import serializers
from patient.models import Patient
from django.contrib.auth.models import User
from .utils import random_password_generator


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        exclude = ["user"]

    def update(self, instance: Any, validated_data: Any) -> Any:
        # patient = Patient.objects.filter(id=instance.i)
        user = patient.user
        if "email" in validated_data:
            user.email = validated_data["email"]
        patient.save()
        user.save()
        return patient


class PatientLoginSerializer(serializers.Serializer):
    username = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100)


class PatientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        exclude = ["user", "id"]

    def create(self, validated_data):
        patient = Patient.objects.create(**validated_data)
        print(validated_data)
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

    def update(self, instance: Any, validated_data: Any) -> Any:
        patient = super().update(instance, validated_data)
        user = patient.user
        user.email = validated_data["email"]
        patient.save()
        user.save()
        return patient
