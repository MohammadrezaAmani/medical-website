from clinic.exercise.api.serializers import ExerciseSerializer
from rest_framework import serializers

from ..models import Prescription

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

    def get_accessories(self, exercise):
        return [equipment.name for equipment in exercise.accessories.all()]

    def get_prescription(self, session):
        return [
            {
                "id": prescription.id,
                "exercises": [
                    {
                        "id": exercise.id,
                        "video": exercise.video,
                        "photo": exercise.photo,
                        "name": exercise.name,
                        "description": exercise.description,
                        "instructions": exercise.instructions,
                        "is_public": exercise.is_public,
                        "keywords": exercise.keywords,
                        "owner": exercise.owner,
                        "placement_position": exercise.placement_position.all(),
                        "target": exercise.target.all(),
                        "target_organs": exercise.target_organs.all(),
                        "displacement": exercise.displacement.all(),
                        "accessories": self.get_accessories(exercise),  # Updated line
                    }
                    for exercise in prescription.exercises.all()
                ],
                "repeat": prescription.repeat,
                "sets": prescription.sets,
                "hold_time": prescription.hold_time,
                "total_time": prescription.total_time,
                "rest_time": prescription.rest_time,
                "patient": prescription.patient,
            }
            for prescription in session.prescription.all()
        ]

    class Meta:
        model = Prescription
        fields = "__all__"
