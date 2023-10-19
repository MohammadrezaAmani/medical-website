from django.db import models
from django.urls import reverse
from doctor.models import Doctor



class Patient(models.Model):
    GENDER_OPTIONS = (("m", "male"), ("f", "female"))
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="images/", null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS)
    birth_date = models.DateField()
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    insurance_number = models.CharField(max_length=10)
    insurance_company = models.CharField(max_length=100)
    injury_date = models.DateField()
    injury_description = models.CharField(max_length=100)
    injury_type = models.CharField(max_length=100)
    medical_documents = models.FileField(upload_to="documents/", null=True, blank=True)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Doctor_detail", kwargs={"pk": self.pk})
