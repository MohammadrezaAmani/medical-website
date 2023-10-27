from rest_framework import serializers
from .models import Prescription
from exercise.serializers import ExerciseSerializer


# class DrugSerializer(serializers.ModelSerializer):
#     """
#     Serializer for the Drug model.
#     """

#     class Meta:
#         model = Drug
#         fields = "__all__"


class PrescriptionSerializer(serializers.ModelSerializer):
    """
    Serializer for Prescription model.
    Includes nested serializers for drugs and exercises.
    """

    # drugs = DrugSerializer(many=True, read_only=True)
    exercises = ExerciseSerializer(many=True, read_only=True)

    class Meta:
        model = Prescription
        fields = "__all__"
