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
    return render(request, "car/analysis.html", context={"describe": describe})


def predict_car(request):
    return render(request, "car/predict_car.html")


def find_car(request):
    brands = get_brands()
    cities = get_cities()
    attributes = get_attributes()
    body_types = get_body_types()
    fuel_types = get_fuel_types()
    wheel_drives = get_wheel_drives()
    colors = get_colors()

    brand = request.GET.get("brand", "")
    year_from = request.GET.get("yearFrom", "")
    year_to = request.GET.get("yearTo", "")
    price_from = request.GET.get("priceFrom", "")
    price_to = request.GET.get("priceTo", "")
    city = request.GET.get("city", "")
    clearenced = request.GET.get("clearenced", "")
    order = request.GET.get("order", "")
    engine_volume_from = request.GET.get("engineFrom", "")
    engine_volume_to = request.GET.get("engineTo", "")
    body_type = request.GET.get("body_type", "")
    fuel_type = request.GET.get("fuel_type", "")
    wheel_drive = request.GET.get("wheel_drive", "")
    color = request.GET.get("color", "")

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

    if city:
        cars = cars.filter(city=city)

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

    cars = cars.filter(custom_clearanced=True)

    if order:
        cars = cars.order_by(order).reverse()
    else:
        cars = cars.order_by("price_difference_percent").reverse()

    if cars.count() > 20:
        cars = cars[:21]

    context = {
        "cars": cars,
        "brands": brands,
        "body_types": body_types,
        "fuel_types": fuel_types,
        "wheel_drives": wheel_drives,
        "colors": colors,
        "cities": cities,
        "attributes": attributes,
    }

    return render(
        request,
        "car/find_car.html",
        context=context,
    )
