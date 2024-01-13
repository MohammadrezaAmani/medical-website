from django.db import models
from django.urls import reverse

from clinic.exercise.models import Exercise


class Prescription(models.Model):
    """
    A model representing a prescription.

    Attributes:
        id (AutoField): The primary key of the prescription.
        drugs (ManyToManyField): The drugs prescribed in the prescription.
        exercises (ManyToManyField): The exercises prescribed in the prescription.
    """

    id = models.AutoField(primary_key=True)
    exercises = models.ManyToManyField(Exercise, blank=True)
    patient = models.ForeignKey("patient.Patient", on_delete=models.CASCADE)
    repeat = models.IntegerField(null=True, blank=True, default=1)
    sets = models.IntegerField(null=True, blank=True, default=1)
    hold_time = models.IntegerField(null=True, blank=True, default=1)
    total_time = models.IntegerField(null=True, blank=True, default=1)
    rest_time = models.IntegerField(null=True, blank=True, default=1)

    def get_absolute_url(self):
        return reverse("Prescription_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"Prescription {self.id}"
