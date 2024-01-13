# serializers.py
from rest_framework import serializers

from .models import PrescriptionReport


class PrescriptionReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrescriptionReport
        fields = ["prescription_id", "pain_level", "repeats", "hardness_present"]


class PrescriptionReportExtendedSerializer(serializers.ModelSerializer):
    """
    Extended serializer for PrescriptionReport model.
    Includes additional information such as prescription ID, exercise details, and the date of the session.
    """

    prescription_id = serializers.SerializerMethodField()
    exercise_details = serializers.SerializerMethodField()
    session_date = serializers.SerializerMethodField()

    class Meta:
        model = PrescriptionReport
        fields = [
            "id",
            "repeats",
            "pain_level",
            "hardness_present",
            "additional_notes",
            "prescription_id",
            "exercise_details",
            "session_date",
            "session_id",
        ]

    def get_prescription_id(self, obj):
        return obj.prescription.id

    def get_exercise_details(self, obj):
        return obj.prescription.exercises.values()

    def get_session_date(self, obj):
        return obj.session.date
