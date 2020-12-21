from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Car(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=30)
    year = models.IntegerField()
    city = models.CharField(max_length=30)
    body_type = models.CharField(max_length=20)
    engine_volume = models.CharField(max_length=7)
    mileage = models.IntegerField()
    gear_type = models.CharField(max_length=20)
    steering_wheel = models.CharField(max_length=5)
    color = models.CharField(max_length=30)
    wheel_drive = models.CharField(max_length=16)
    custom_clearanced = models.BooleanField(default=True)
    price = models.IntegerField()
    average_price = models.IntegerField()
    link = models.CharField(max_length=40)
    fuel_type = models.CharField(max_length=8)
    favourite = models.ManyToManyField(User, related_name='favourite', blank=True)

    def __str__(self):
        return self.brand + " " + self.model + " " + self.city + " id: " + str(self.id)

    def get_name(self):
        return self.brand + " " + self.model + " (" + str(self.year) + ")"

    def get_absolute_url(self):
        return reverse("car_detail_url", kwargs={"id": self.id})




