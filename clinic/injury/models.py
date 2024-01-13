from django.db import models


# Create your models here.
class Injury(models.Model):
    injury_type = models.CharField(max_length=100)
    injury_description = models.CharField(max_length=100)

    def __str__(self):
        return self.injury_type
