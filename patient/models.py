from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from doctor.models import Doctor


class Patient(models.Model):
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
    name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    username = models.CharField(max_length=100, unique=True)
    photo = models.ImageField(upload_to="images/", null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    insurance_number = models.CharField(max_length=10, null=True, blank=True)
    insurance_company = models.CharField(max_length=100, null=True, blank=True)
    injury_date = models.DateField(null=True, blank=True)
    injury_description = models.CharField(max_length=100, null=True, blank=True)
    injury_type = models.CharField(max_length=100)
    medical_documents = models.FileField(upload_to="documents/", null=True, blank=True)
    is_active = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Patient_detail", kwargs={"pk": self.pk})
