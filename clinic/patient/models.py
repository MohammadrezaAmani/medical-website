from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from clinic.doctor.models import Doctor


class Patient(models.Model):

    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(max_length=11, unique=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="patient_profile",
        null=True,
        blank=True,
    )
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name="patients", null=True, blank=True
    )
    GENDER_OPTIONS = (("m", "Male"), ("f", "Female"))
    password = models.CharField(max_length=100, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    photo = models.ImageField(upload_to="images/", null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    insurance_number = models.CharField(max_length=10, null=True, blank=True)
    insurance_company = models.CharField(max_length=100, null=True, blank=True)
    injury_date = models.DateField(null=True, blank=True)
    injury_description = models.CharField(max_length=100, null=True, blank=True)
    injury_type = models.CharField(max_length=100)
    medical_documents = models.FileField(upload_to="documents/", null=True, blank=True)
    blood_type = models.CharField(max_length=10, null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name + " " + self.last_name

    def get_absolute_url(self):
        return reverse("Patient_detail", kwargs={"pk": self.pk})
