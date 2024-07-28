from django.db import models
from django.core.exceptions import ValidationError as v
from car_app.models import Car

# Create your models here.
class Service_record(models.Model):
    date = models.DateField(blank=False, null=False)
    reason = models.CharField(blank=False, null=False)
    completed = models.BooleanField(blank=False, default=False)
    place_of_service = models.CharField(blank=False)
    notes = models.TextField()
    vehicles = models.ForeignKey(Car, related_name='service_record', on_delete=models.CASCADE)
    