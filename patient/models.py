from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from doctor.models import Doctor
# Create your models here.


class Patient(models.Model):
    GENDER_OPTIONS = (
        ('m','male'),
        ('f','female')
    )
    gender = models.CharField(max_length=1,choices=GENDER_OPTIONS)
    birth_date = models.DateField()
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    insurance_number = models.CharField(max_length=10)
    insurance_company = models.CharField(max_length=100)
    injury_date = models.DateField()
    injury_description = models.CharField(max_length=100)
    injury_type = models.CharField(max_length=100)
    medical_documents = models.FileField(upload_to='documents/',null=True,blank=True)
    # medical_images = models.ImageField(upload_to='images/',null=True,blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Doctor_detail", kwargs={"pk": self.pk})
