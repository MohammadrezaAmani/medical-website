from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from clinic.doctor.models import Doctor
from clinic.injury.models import Injury
from clinic.insurance.models import Insurance

User = get_user_model()


class PateintDoctor(models.Model):
    patient = models.ForeignKey("patient.Patient", on_delete=models.CASCADE)
    doctor = models.ForeignKey("doctor.Doctor", on_delete=models.CASCADE)
    injury = models.ManyToManyField(Injury)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    doctor = models.ManyToManyField(Doctor, through=PateintDoctor)
    medical_documents = models.FileField(
        upload_to="files/documents/", null=True, blank=True
    )
    blood_type = models.CharField(max_length=10, null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " " + self.last_name

    def get_absolute_url(self):
        return reverse("Patient_detail", kwargs={"pk": self.pk})
