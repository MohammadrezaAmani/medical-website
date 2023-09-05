from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)


class DoctorUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    Gender_Chocies = (
        ("m", "Male"),
        ("f", "female"),
    )
    gender = models.CharField(max_length=1, choices=Gender_Chocies, default="m")
    id = models.AutoField(primary_key=True)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def get_patients(self):
        return PatientUser.objects.filter(doctors__id=self.id)


class PatientUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    id = models.AutoField(primary_key=True)
    doctors = models.ManyToManyField(DoctorUser)
    injuries = models.ManyToManyField("Injuries", blank=True)
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]
    Gender_Chocies = (
        ("m", "Male"),
        ("f", "female"),
    )
    gender = models.CharField(max_length=1, choices=Gender_Chocies, default="m")
    id = models.AutoField(primary_key=True)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    Blood_Type_Choices = (
        ("a+", "A+"),
        ("a-", "A-"),
        ("b+", "B+"),
        ("b-", "B-"),
        ("ab+", "AB+"),
        ("ab-", "AB-"),
        ("o+", "O+"),
        ("o-", "O-"),
    )
    blood_type = models.CharField(
        max_length=3, choices=Blood_Type_Choices, default="a+"
    )


class Injuries(models.Model):
    injury_name = models.CharField(max_length=30)
    injury_description = models.CharField(max_length=1000)
    injury_image = models.ImageField(upload_to="injury_images/", null=True, blank=True)

    def __str__(self):
        return self.injury_name
