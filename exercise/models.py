from django.db import models
from django.urls import reverse


# Create your models here.
class Exercise(models.Model):
    id = models.AutoField(primary_key=True)
    video = models.FileField(upload_to="videos/", null=True, blank=True)
    photo = models.ImageField(upload_to="images/", null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    placement_position = models.CharField(max_length=100)
    target = models.TextField(blank=True, null=True)
    target_organs = models.CharField(max_length=100)
    displacement = models.CharField(max_length=100)
    instructions = models.TextField(blank=True, null=True)
    accessories = models.TextField(blank=True, null=True)
    is_public = models.BooleanField(default=False)  # True if public, False if private

    # class Meta:
    #     verbose_name = _("Exercise")
    #     verbose_name_plural = _("Exercises")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Exercise_detail", kwargs={"pk": self.pk})


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    # class Meta:
    #     verbose_name = _("Equipment")
    #     verbose_name_plural = _("Equipments")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Equipment_detail", kwargs={"pk": self.pk})


class Goal(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    # class Meta:
    #     verbose_name = _("Goal")
    #     verbose_name_plural = _("Goals")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Goal_detail", kwargs={"pk": self.pk})


class Displacement(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    # class Meta:
    #     verbose_name = _("Displacement")
    #     verbose_name_plural = _("Displacements")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Displacement_detail", kwargs={"pk": self.pk})


class PlacementPosition(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("PlacementPosition_detail", kwargs={"pk": self.pk})
