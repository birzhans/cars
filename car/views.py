from django.shortcuts import render
from .models import Car

# Create your views here.
def index(request):
    cars = Car.objects.all()[:10]
    return render(request, "car/index.html", context={"cars": cars})
