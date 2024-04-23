from django.db import models


class VehiclesForRent(models.Model):
    vehicle_image = models.ImageField(upload_to='vehicles_images', null=True, blank=True)
    logo = models.ImageField(upload_to='vehicles_logo', null=True, blank=True)
    mark = models.CharField(max_length=65, unique=True, blank=True)
    model = models.CharField(max_length=65, unique=True, blank=True)
    color = models.CharField(max_length=65, blank=True)
    type = models.CharField(max_length=15, blank=True)
    engine_val = models.FloatField(blank=True, default=0.0)
    fuel_type = models.CharField(max_length=25, blank=True)
    gear_box = models.CharField(max_length=25, blank=True)
    year = models.IntegerField(blank=True, default=0)
    title = models.CharField(max_length=255, blank=True)
    about_vehicle = models.TextField(blank=True)
    price = models.FloatField(null=True, default=0.0)
    available = models.BooleanField(default=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    

    def __str__(self) -> str:
        return f"Mark: {self.mark}. | Model: {self.model}. | ID: {self.id}"