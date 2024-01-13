from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

User = get_user_model()


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    medical_system_code = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return str(self.name) + " " + (self.last_name)

    def get_absolute_url(self):
        return reverse("Doctor_detail", kwargs={"pk": self.pk})
