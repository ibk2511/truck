from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, null=False, blank=False)
    aadhar_id = models.CharField(max_length=16, null=False, blank=False)


class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10, null=False, blank=False)
    aadhar_id = models.CharField(max_length=16, null=False, blank=False)


class Truck(models.Model):
    owner = models.OneToOneField(Owner,on_delete=models.CASCADE, default=None)
    model = models.CharField(max_length=20, null=False, blank=False)
    make = models.CharField(max_length=20, null=False, blank=False)
    capacity = models.FloatField(default=0, null=False, blank=False)
    wheels = models.PositiveSmallIntegerField(default=0, null=False, blank=False)
    is_rented = models.BooleanField(default=False)
    rate_per_day = models.IntegerField(null=False, blank=False)
    is_requested = models.BooleanField(default=False)


class TruckRent(models.Model):
    is_verified = models.BooleanField(default=False)
    truck = models.ForeignKey(Truck, on_delete=models.CASCADE)
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    pickup_time = models.DateTimeField(default=None,blank=True,null=True)
    drop_time = models.DateTimeField(default=None,blank=True,null=True)
    is_dropped = models.BooleanField(default=False)
