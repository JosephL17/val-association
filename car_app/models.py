from django.db import models
from django.core import validators as v
from engine_app.models import Engine
from owner_app.models import Owner

# Create your models here.
class Car(models.Model):
    make = models.CharField(max_length=55, blank=False, null=False)
    model = models.CharField(max_length=55, blank=False, null=False)
    mileage = models.IntegerField(blank=False, null=False, validators=[v.MinValueValidator(0)])
    year = models.IntegerField(blank=False, null=False)
    owners = models.ManyToManyField(Owner, related_name='car')
    number_of_tires = models.IntegerField(null=False, blank=False,  validators=[v.MinValueValidator(0)])
    engine = models.OneToOneField (Engine, on_delete=models.CASCADE)


