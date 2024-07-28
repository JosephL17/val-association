from django.db import models
from car_app.models import Car

# Create your models here.
class Tires(models.Model):
    section_width = models.BigIntegerField(blank=False)
    aspect_ratio = models.BigIntegerField(blank=False)
    rim_size = models.BigIntegerField(blank=False)
    vehicle_type = models.CharField(blank=False)
    vehicle = models.OneToOneField(Car, related_name="car", on_delete=models.CASCADE)