from django.db import models
from django.urls import reverse

# from django.contrib.auth.models import User

# Create your models here.


class Doctor(models.Model):
    GENDER_OPTIONS = (("m", "male"), ("f", "female"))
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
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Doctor_detail", kwargs={"pk": self.pk})
