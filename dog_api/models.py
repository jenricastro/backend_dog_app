from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=32)
    breed = models.CharField(max_length=32)
    gender = models.CharField(max_length=32)
    color = models.CharField(max_length=32)
    size = models.CharField(max_length=32)
    age = models.IntegerField()
    description = models.CharField(max_length=60)
    image_url = models.CharField(max_length=200, blank=True) #store url pics