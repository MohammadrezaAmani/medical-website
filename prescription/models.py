from django.db import models
from django.urls import reverse
from exercise.models import Exercise


class Prescription(models.Model):
    id = models.AutoField(primary_key=True)
    drugs = models.ManyToManyField("Drug", blank=True)
    exercises = models.ManyToManyField(Exercise, blank=True)

    def get_absolute_url(self):
        return reverse("Prescription_detail", kwargs={"pk": self.pk})


class Drug(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    others = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Drug_detail", kwargs={"pk": self.pk})
