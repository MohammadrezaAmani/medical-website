from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from doctor.models import Doctor


class Patient(models.Model):
    """
    A model representing a patient in the system.

    Attributes:
        id (int): The unique identifier for the patient.
        user (User): The user associated with the patient.
        doctor (Doctor): The doctor associated with the patient.
        password (str): The password for the patient.
        name (str): The first name of the patient.
        last_name (str): The last name of the patient.
        email (str): The email address of the patient.
        photo (ImageField): The profile picture of the patient.
        bio (str): The bio of the patient.
        gender (str): The gender of the patient.
        birth_date (date): The birth date of the patient.
        address (str): The address of the patient.
        phone_number (str): The phone number of the patient.
        insurance_number (str): The insurance number of the patient.
        insurance_company (str): The insurance company of the patient.
        injury_date (date): The date of injury of the patient.
        injury_description (str): The description of the injury of the patient.
        injury_type (str): The type of injury of the patient.
        medical_documents (FileField): The medical documents of the patient.
        blood_type (str): The blood type of the patient.
        height (float): The height of the patient.
        weight (float): The weight of the patient.
    """

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
        return self.name+" "+self.last_name

    def get_absolute_url(self):
        return reverse("Patient_detail", kwargs={"pk": self.pk})
