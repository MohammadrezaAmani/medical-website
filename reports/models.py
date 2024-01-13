from django.db import models

from prescription.models import Prescription
from session.models import Session


class PrescriptionReport(models.Model):
    """
    A model representing a report for a prescription after a session.

    Attributes:
        id (AutoField): The primary key of the report.
        prescription (ForeignKey): The prescription associated with the report.
        session (ForeignKey): The session associated with the report.
        repeats (IntegerField): The number of repeats performed by the patient.
        pain_level (CharField): The pain level reported by the patient.
        hardness_present (CharField): The hardness level reported by the patient.
        additional_notes (TextField): Additional notes provided by the patient.
    """

    id = models.AutoField(primary_key=True)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    repeats = models.FloatField()
    pain_level = models.FloatField()
    hardness_present = models.FloatField()
    additional_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Report for Prescription {self.prescription.id} in Session {self.session.id}"
