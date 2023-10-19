from rest_framework import serializers
from .models import Prescription, Drug
from exercise.serializers import ExerciseSerializer


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
