from django.contrib.auth.models import AbstractUser, BaseUserManager, Permission
from django.db import models


class BaseUser(models.Model):
    GENDER_OPTIONS = (("m", "Male"), ("f", "Female"))
    photo = models.ImageField(upload_to="media/images/", null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_OPTIONS, default="m")
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        abstract = True


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(username, email, password, **extra_fields)


class CustomUser(BaseUser, AbstractUser):
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",
        blank=True,
        verbose_name="groups",
        help_text="The groups this user belongs to.",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_set",
        blank=True,
        verbose_name="user permissions",
        help_text="Specific permissions for this user.",
    )

    objects = CustomUserManager()

    class Meta:
        pass
