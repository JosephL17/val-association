from django.db import models
from django.core import validators as v
# Create your models here.

class Engine(models.Model):
    size = models.IntegerField(blank=False, null=False)
    custome = models.BooleanField(default=False)


