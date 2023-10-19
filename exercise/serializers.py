from rest_framework import serializers
from .models import (
    Equipment,
    Goal,
    Displacement,
    PlacementPosition,
    Target,
    Organ,
    Exercise,
)


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = "__all__"


class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = "__all__"


class DisplacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Displacement
        fields = "__all__"


class PlacementPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacementPosition
        fields = "__all__"


class TargetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Target
        fields = "__all__"


class OrganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organ
        fields = "__all__"


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = "__all__"
