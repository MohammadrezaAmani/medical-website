from rest_framework import serializers
from .models import Prescription, Drug
from exercise.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"


class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        fields = "__all__"


class PrescriptionSerializer(serializers.ModelSerializer):
    drugs = DrugSerializer(many=True, read_only=True)
    exercises = ExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = Prescription
        fields = "__all__"
