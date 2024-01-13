from django.db import models
from django.urls import reverse

from clinic.patient.models import Patient
from clinic.prescription.models import Prescription


class Session(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescription = models.ManyToManyField(Prescription)
    date = models.DateField()
    time = models.TimeField()
    SESSION_TYPE = (
        ("online", "online"),
        ("offline", "offline"),
    )
    session_type = models.CharField(max_length=7, choices=SESSION_TYPE, null=True)
    SESSION_OPTION = (
        ("p", "pending"),
        ("c", "completed"),
    )
    status = models.CharField(max_length=1, choices=SESSION_OPTION)
    rate = models.IntegerField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "session" + " " + str(self.date)

    def get_absolute_url(self):
        return reverse("Session_detail", kwargs={"pk": self.pk})

    def doctor(self):
        return self.patient.doctor
