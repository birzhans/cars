from django.shortcuts import render
from .models import Car
from .constants import *

from .anal import *

# Create your views here.
def index(request):
    cars = Car.objects.all()[:21]
    return render(request, "car/index.html", context={"cars": cars})


def car_detail(request, id):
    car = Car.objects.get(id__iexact=id)
    return render(request, "car/car_detail.html", context={"car": car})


def analysis(request):
    describe = data.describe()
    return render(request, "car/predict_car.html", context={"describe": describe})


def predict_car(request):
    return render(request, "car/predict_car.html")


def find_car(request):
    brands = get_brands()
    brand = request.GET.get("brand", "")
    year_from = request.GET.get("yearFrom", "")
    year_to = request.GET.get("yearTo", "")
    price_from = request.GET.get("priceFrom", "")
    price_to = request.GET.get("priceTo", "")

    cars = Car.objects.all()

    if brand:
        cars = cars.filter(brand=brand)

    if year_from:
        cars = cars.filter(year__gte=int(year_from))

    if year_to:
        cars = cars.filter(year__lte=int(year_to))

    if price_from:
        cars = cars.filter(price__gte=int(price_from))

    if price_to:
        cars = cars.filter(price__lte=int(price_to))

    if cars.count() > 20:
        cars = cars[:20]

    return render(
        request, "car/find_car.html", context={"cars": cars, "brands": brands}
    )
