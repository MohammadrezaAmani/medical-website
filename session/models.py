from django.db import models
from prescription.models import Prescription
from patient.models import Patient

from django.urls import reverse


# Create your models here.
class Session(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    session_type = models.CharField(max_length=100)
    SESSION_OPTION = (
        ("p", "pending"),
        ("c", "completed"),
    )
    status = models.CharField(max_length=1, choices=SESSION_OPTION)
    rate = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    # class Meta:
    #     verbose_name = _("Session")
    #     verbose_name_plural = _("Sessions")

    # def __str__(self):
    #     return self.name

    def get_absolute_url(self):
        return reverse("Session_detail", kwargs={"pk": self.pk})
