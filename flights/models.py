from django.db import models
from django.contrib.auth.models import User

class Stops(models.Model):
    location = models.CharField(max_length=255)
class Times(models.Model):
    time = models.TimeField()
class Dates(models.Model):
    date = models.DateField()
class Flights(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cost = models.CharField(max_length=255)
    times = models.ManyToManyField(Times)
    dates = models.ManyToManyField(Dates)
    stops = models.ManyToManyField(Stops)
class CopyFlight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cost = models.CharField(max_length=255)
    times = models.ManyToManyField(Times)
    dates = models.ManyToManyField(Dates)
    stops = models.ManyToManyField(Stops)
class MyFlight(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    rest = models.ManyToManyField(CopyFlight)
