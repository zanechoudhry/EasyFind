from django.db import models
from django.contrib.auth.models import User
from food.models import Restaurants

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_picture = models.ImageField(default="yoda.png", null=True, blank=True)
