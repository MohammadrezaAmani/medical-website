from django.db import models
from django.urls import reverse
from exercise.models import Exercise


class Prescription(models.Model):
    """
    A model representing a prescription.

    Attributes:
        id (AutoField): The primary key of the prescription.
        drugs (ManyToManyField): The drugs prescribed in the prescription.
        exercises (ManyToManyField): The exercises prescribed in the prescription.
    """

    id = models.AutoField(primary_key=True)
    # drugs = models.ManyToManyField("Drug", blank=True)
    exercises = models.ManyToManyField(Exercise, blank=True)
    patient = models.ForeignKey('patient.Patient', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("Prescription_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"Prescription {self.id}"


# class Drug(models.Model):
#     """
#     A model representing a drug.

#     Attributes:
#         id (int): The primary key of the drug.
#         name (str): The name of the drug.
#         description (str, optional): A description of the drug.
#         others (dict, optional): A JSON field for any additional information about the drug.
#     """

#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True)
#     others = models.JSONField(blank=True, null=True)

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("Drug_detail", kwargs={"pk": self.pk})
