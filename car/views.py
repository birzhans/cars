from django.shortcuts import render
from .models import Car

# Create your views here.
def index(request):
    cars = Car.objects.all()[:100]
    return render(request, "car/index.html", context={"cars": cars})


def car_detail(request, id):
    car = Car.objects.get(id__iexact=id)
    return render(request, "car/car_detail.html", context={"car": car})


def find_car(request):
    brands = ["Audi", "BMW"]
    brand = request.GET.get("brand", "")

    if brand:
        cars = Car.objects.filter(brand__icontains=brand)[:20]
    else:
        cars = Car.objects.all()[:20]
    return render(
        request, "car/find_car.html", context={"cars": cars, "brands": brands}
    )


def predict_car(request):
    return render(request, "car/predict_car.html")
