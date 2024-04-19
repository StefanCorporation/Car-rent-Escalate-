from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from vehicles.models import VehiclesForRent


class Users(AbstractUser):
    image = models.ImageField(upload_to='users_profile_images', null=True, blank=True)
    


class RentData(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default=None)
    vehicle_for_rent = models.ForeignKey(VehiclesForRent, on_delete=models.CASCADE, default=None)
    username = models.CharField(max_length=55, null=True, blank=True)
    email = models.CharField(max_length=150, null=True, blank=True)
    first_name = models.CharField(max_length=55, null=True, blank=True)
    last_name = models.CharField(max_length=55, null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    pick_up_location = models.CharField(max_length=55, null=True, blank=True)
    leave_car_location = models.CharField(max_length=55, null=True, blank=True)
    pick_up_time = models.TimeField(default=0.0, null=True, blank=True)
    return_time = models.TimeField(default=0.0, null=True, blank=True)
    pick_up_date = models.DateField(null=True, blank=True)
    car_return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Rent check for {self.user.username}"
    

