from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .models import Car
from .constants import get_brands, get_body_types, get_fuel_types, get_wheel_drives, get_colors

from .anal import *

# Create your views here.


@login_required
def favorite_car(request, id):
    car = get_object_or_404(Car, id=id)
    if car.favourite.filter(id=request.user.id).exists():
        car.favourite.remove(request.user)
    else:
        car.favourite.add(request.user)
    return HttpResponseRedirect(car.get_absolute_url())

def index(request):
    cars = Car.objects.all()[:100]
    return render(request, "car/index.html", context={"cars": cars})


def car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    is_favourite = False

    if car.favourite.filter(id=request.user.id).exists():
        is_favourite = True

    return render(request, "car/car_detail.html", context={"car": car, "is_favourite": is_favourite})


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
    body_types = get_body_types()
    body_type = request.GET.get("body_type", "")
    fuel_types = get_fuel_types()
    fuel_type = request.GET.get("fuel_type", "")
    wheel_drives = get_wheel_drives()
    wheel_drive = request.GET.get('wheel_drive', "")
    colors = get_colors()
    color = request.GET.get("color", "")
    engine_volume_from = request.GET.get("engineFrom", "")
    engine_volume_to = request.GET.get("engineTo", "")


    cars = Car.objects.all()

    if engine_volume_from:
        cars = cars.filter(engine_volume__gte=float(engine_volume_from))

    if engine_volume_to:
        cars = cars.filter(engine_volume__lte=float(engine_volume_to))

    if color:
        cars = cars.filter(color=color)

    if wheel_drive:
        cars = cars.filter(wheel_drive=wheel_drive)

    if fuel_type:
        cars = cars.filter(fuel_type=fuel_type)

    if body_type:
        cars = cars.filter(body_type=body_type)

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

    context = {"cars": cars,
               "brands": brands,
               'body_types': body_types,
               'fuel_types': fuel_types,
               'wheel_drives': wheel_drives,
               'colors': colors, }


    return render(
        request, "car/find_car.html", context
    )
