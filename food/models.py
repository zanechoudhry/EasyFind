from django.db import models
from django.contrib.auth.models import User

class Restaurants(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 255)
    rating = models.IntegerField()
    num_reviews = models.IntegerField()
    url = models.CharField(max_length = 255)
    address = models.CharField(max_length = 255, null = True)
    zip_code = models.IntegerField()
    city = models.CharField(max_length = 255)
    price = models.CharField(max_length=5)
