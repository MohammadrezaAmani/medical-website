from django.db import models
from django.urls import reverse


class Equipment(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Equipment_detail", kwargs={"pk": self.pk})


class Goal(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Goal_detail", kwargs={"pk": self.pk})


class Displacement(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Displacement_detail", kwargs={"pk": self.pk})


class PlacementPosition(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("PlacementPosition_detail", kwargs={"pk": self.pk})


class Target(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Target_detail", kwargs={"pk": self.pk})


class Organ(models.Model):
    name = models.CharField(max_length=100, unique=True)
    photo = models.ImageField(upload_to="images/", null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Organ_detail", kwargs={"pk": self.pk})


class Exercise(models.Model):
    owner = models.ForeignKey("doctor.Doctor", on_delete=models.CASCADE,
                              null=True, blank=True)
    video = models.FileField(upload_to="videos/", null=True, blank=True)
    photo = models.ImageField(upload_to="images/", null=True, blank=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    placement_position = models.ManyToManyField(PlacementPosition, blank=True)
    target = models.ManyToManyField(Target, blank=True)
    target_organs = models.ManyToManyField(Organ, blank=True)
    displacement = models.ManyToManyField(Displacement, blank=True)
    instructions = models.TextField(blank=True, null=True)
    accessories = models.ManyToManyField(Equipment, blank=True)
    is_public = models.BooleanField(default=False)
    keywords = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Exercise_detail", kwargs={"pk": self.pk})
