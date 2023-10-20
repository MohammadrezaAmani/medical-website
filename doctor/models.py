from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="doctor_profile"
    )
    GENDER_OPTIONS = (("m", "Male"), ("f", "Female"))
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="images/", null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS)
    birth_date = models.DateField()
    medical_system_code = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Doctor_detail", kwargs={"pk": self.pk})


class Patient(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="patient_profile"
    )
    GENDER_OPTIONS = (("m", "Male"), ("f", "Female"))
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="images/", null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS)
    birth_date = models.DateField()
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    insurance_number = models.CharField(max_length=10)
    insurance_company = models.CharField(max_length=100)
    injury_date = models.DateField()
    injury_description = models.CharField(max_length=100)
    injury_type = models.CharField(max_length=100)
    medical_documents = models.FileField(upload_to="documents/", null=True, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Patient_detail", kwargs={"pk": self.pk})
