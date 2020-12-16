from django.shortcuts import render
from .models import Car

# Create your views here.
def index(request):
    cars = Car.objects.all()[:100]
    return render(request, "car/index.html", context={"cars": cars})


def car_detail(request, id):
    car = Car.objects.get(id__iexact=id)
    return render(request, "car/car_detail.html", context={"car": car})
