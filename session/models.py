from django.db import models
from prescription.models import Prescription
from patient.models import Patient

from django.urls import reverse


class Session(models.Model):
    """
    A model representing a session between a patient and a doctor.

    Attributes:
        id (AutoField): The primary key of the session.
        patient (ForeignKey): The patient associated with the session.
        prescription (ManyToManyField): The prescriptions associated with the session.
        date (DateField): The date of the session.
        time (TimeField): The time of the session.
        session_type (CharField): The type of the session.
        status (CharField): The status of the session.
        rate (IntegerField): The rating of the session.
        description (TextField): The description of the session.
    """

    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescription = models.ManyToManyField(Prescription)
    date = models.DateField()
    time = models.TimeField()
    SESSION_TYPE=(
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
        return "session"+" "+str(self.date)

    def get_absolute_url(self):
        return reverse("Session_detail", kwargs={"pk": self.pk})

    def doctor(self):
        return self.patient.doctor
