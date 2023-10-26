from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


class Doctor(models.Model):
    """
    A model representing a doctor in the system.

    Attributes:
    -----------
    id : int
        The unique identifier for the doctor.
    username : str
        The username - phone number of the doctor.
    password : str
        The password of the doctor.
    email : str
        The email address of the doctor.
    user : User
        The user associated with the doctor.
    name : str
        The first name of the doctor.
    last_name : str
        The last name of the doctor.
    photo : ImageField
        The profile picture of the doctor.
    bio : str
        The biography of the doctor.
    gender : str
        The gender of the doctor.
    birth_date : DateField
        The birth date of the doctor.
    medical_system_code : str
        The medical system code of the doctor.
    address : str
        The address of the doctor.
    phone_number : str
        The phone number of the doctor.
    created_at : DateTimeField
        The date and time when the doctor was created.
    updated_at : DateTimeField
        The date and time when the doctor was last updated.
    """

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
    photo = models.ImageField(upload_to="images/", null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS, default="m")
    birth_date = models.DateField(null=True, blank=True)
    medical_system_code = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Doctor_detail", kwargs={"pk": self.pk})


@receiver(post_save, sender=Doctor)
def create_user(sender, instance, created, **kwargs):
    """
    Creates a new user instance and sets its password.
     If the user already exists, updates the user's username, email, and password.

    Args:
        sender: The model class.
        instance: The actual instance being saved.
        created: A boolean indicating whether the instance was just created.
        **kwargs: Additional keyword arguments.

    Returns:
        None
    """
    if created:
        user = User.objects.create(username=instance.username, email=instance.email)
        user.set_password(instance.password)
        instance.user = user
        instance.user.save()
        instance.save()
    else:
        instance.user.username = instance.username
        instance.user.set_password(instance.password)
        print(instance.user.password)
        instance.user.email = instance.email
        instance.user.save()
