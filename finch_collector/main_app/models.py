from django.db import models
from django.urls import reverse
import datetime


# Create your models here.


class Camera(models.Model):
    name = models.CharField(max_length=100, default="Canon")
    price = models.IntegerField(default=1000)
    resolution = models.CharField(max_length=100, default="20MP")
    image = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})


# One to many relationship with Camera, define FK as just the base class name, _id added later
class Photo(models.Model):
    name = models.CharField(max_length=50, default="")
    url = models.CharField(max_length=250, default="")
    camera = models.ForeignKey(Camera, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Gear(models.Model):
    name = models.CharField(max_length=100, default="")
    price = models.IntegerField(default=100)
