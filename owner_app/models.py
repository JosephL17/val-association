from django.db import models
from django.core import validators as v
# Create your models here.

class Owner(models.Model):
    age = models.IntegerField(blank=False, null=False)
    address = models.CharField(blank=False, null=False)
    name = models.CharField(blank=False, null=False)
    num_of_vehicles = models.IntegerField(blank=False, null=False)