from django.db import models
from django.urls import reverse


class Equipment(models.Model):
    """
    A model representing an equipment.

    Attributes:
        name (str): The name of the equipment.
    """

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Equipment_detail", kwargs={"pk": self.pk})


class Goal(models.Model):
    """
    A model representing a goal.

    Attributes:
    - name (str): The name of the goal.

    Methods:
    - __str__(): Returns the name of the goal.
    - get_absolute_url(): Returns the URL of the goal detail page.
    """

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Goal_detail", kwargs={"pk": self.pk})


class Displacement(models.Model):
    """
    A model representing a displacement.

    Attributes:
        name (str): The name of the displacement.
    """

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Displacement_detail", kwargs={"pk": self.pk})


class PlacementPosition(models.Model):
    """
    A model representing a placement position.

    Attributes:
        name (str): The name of the placement position.
    """

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("PlacementPosition_detail", kwargs={"pk": self.pk})


class Target(models.Model):
    """
    A model representing a target.

    Attributes:
        name (str): The name of the target.
    """

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Target_detail", kwargs={"pk": self.pk})


class Organ(models.Model):
    """
    A model representing an organ in the human body.

    Attributes:
        name (str): The name of the organ.
        photo (ImageField): An image of the organ.
        description (str): A description of the organ.
    """

    name = models.CharField(max_length=100, unique=True)
    photo = models.ImageField(upload_to="images/", null=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Organ_detail", kwargs={"pk": self.pk})


class Exercise(models.Model):
    """
    A model representing an exercise.

    Attributes:
        owner (ForeignKey): A foreign key to the Doctor model.
        video (FileField): A file field for uploading videos.
        photo (ImageField): An image field for uploading photos.
        name (CharField): A character field for the name of the exercise.
        description (TextField): A text field for the description of the exercise.
        placement_position (ManyToManyField): A many-to-many field for the placement position of the exercise.
        target (ManyToManyField): A many-to-many field for the target of the exercise.
        target_organs (ManyToManyField): A many-to-many field for the target organs of the exercise.
        displacement (ManyToManyField): A many-to-many field for the displacement of the exercise.
        instructions (TextField): A text field for the instructions of the exercise.
        accessories (ManyToManyField): A many-to-many field for the equipment/accessories of the exercise.
        is_public (BooleanField): A boolean field indicating whether the exercise is public or not.
        keywords (TextField): A text field for the keywords of the exercise.
    """

    owner = models.ForeignKey(
        "doctor.Doctor", on_delete=models.CASCADE, null=True, blank=True
    )
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
