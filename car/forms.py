from django import forms

class FindForm(forms.Form):
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

	