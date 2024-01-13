from django.db import models


# Create your models here.
class Insurance(models.Model):
    insurance_name = models.CharField(max_length=100)
    insurance_description = models.CharField(max_length=100)

    def __str__(self):
        return self.insurance_name
