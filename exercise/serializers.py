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
    """
    A serializer for the Equipment model.

    This serializer serializes and deserializes Equipment model instances
    to and from JSON format. It includes all fields of the Equipment model.

    Attributes:
        Meta: A class that contains metadata about the serializer.
            In this case, it specifies the model to use and the fields to include.
    """

    class Meta:
        model = Equipment
        fields = "__all__"


class GoalSerializer(serializers.ModelSerializer):
    """
    Serializer for Goal model.

    Serializes the Goal model to and from JSON format. This serializer
    includes all fields of the Goal model.

    Attributes:
        Meta: A class that contains metadata about the serializer, such as
            the model to use and the fields to include.
    """

    class Meta:
        model = Goal
        fields = "__all__"


class DisplacementSerializer(serializers.ModelSerializer):
    """
    Serializer for Displacement model.

    Serializes the Displacement model to and from JSON format.

    Fields:
    - model: The Displacement model to be serialized.
    - fields: The fields to be included in the serialized output. If set to "__all__", all fields will be included.
    """

    class Meta:
        model = Displacement
        fields = "__all__"


class PlacementPositionSerializer(serializers.ModelSerializer):
    """
    Serializer for PlacementPosition model.

    This serializer is used to convert PlacementPosition model instances to JSON format and vice versa.
    It includes all fields of the PlacementPosition model.

    Attributes:
        Meta: A class that contains metadata about the serializer, including the model to serialize and the fields to include.
    """

    class Meta:
        model = PlacementPosition
        fields = "__all__"


class TargetSerializer(serializers.ModelSerializer):
    """
    A serializer for the Target model.

    This serializer is used to convert Target model instances to Python
    data types, which can then be easily rendered into JSON or other content
    types. It also handles deserialization, allowing parsed data to be
    converted back into complex types, after first validating the incoming
    data.

    Attributes:
        Meta: A class that contains metadata about the serializer, such as
            the model it is associated with and the fields to include.
    """

    class Meta:
        model = Target
        fields = "__all__"


class OrganSerializer(serializers.ModelSerializer):
    """
    Serializer for Organ model.

    This serializer serializes and deserializes Organ model instances
    to and from JSON format. It includes all fields of the Organ model.

    Attributes:
        Meta: A class that contains metadata about the serializer.
            In this case, it specifies the model to use and the fields to include.
    """

    class Meta:
        model = Organ
        fields = "__all__"


class ExerciseSerializer(serializers.ModelSerializer):
    """
    Serializer for Exercise model.

    This serializer serializes and deserializes Exercise model instances
    to and from JSON format. It includes all fields of the Exercise model.

    Attributes:
        Meta: A class that contains metadata about the serializer.
            In this case, it specifies the model to use and the fields to include.
    """

    class Meta:
        model = Exercise
        fields = "__all__"


class ExerciseCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating Exercise model.

    This serializer is used to create new Exercise model instances.
    It excludes the "owner" field from the serialized output.

    Attributes:
        Meta: A class that contains metadata about the serializer.
            In this case, it specifies the model to use and the fields to exclude.
    """

    class Meta:
        model = Exercise
        exclude = "owner"
