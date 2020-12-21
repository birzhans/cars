from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from car.models import Car

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    favourite = models.ManyToManyField(Car)
