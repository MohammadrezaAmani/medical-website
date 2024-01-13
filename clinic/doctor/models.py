from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Doctor(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=12, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="doctor_profile",
        null=True,
        blank=True,
    )
    GENDER_OPTIONS = (("m", "Male"), ("f", "Female"))
    name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(upload_to="media/images/", null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS, default="m")
    birth_date = models.DateField(null=True, blank=True)
    medical_system_code = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.name) + " " + (self.last_name)

    def get_absolute_url(self):
        return reverse("Doctor_detail", kwargs={"pk": self.pk})