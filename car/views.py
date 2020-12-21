from django.shortcuts import render
from .models import Car
from .constants import *
from .predict import *
from .anal import *

# Create your views here.
def index(request):
    cars = Car.objects.all()[:21]
    return render(request, "car/index.html", context={"cars": cars})


def car_detail(request, id):
    car = Car.objects.get(id__iexact=id)
    return render(request, "car/car_detail.html", context={"car": car})


def analysis(request):
    return render(request, "car/analysis.html")


def predict_car(request):
    brands = get_brands()
    cities = get_cities()
    attributes = get_attributes()
    body_types = get_body_types()
    fuel_types = get_fuel_types()
    wheel_drives = get_wheel_drives()
    colors = get_colors()
    gear_types = get_gear_type()
    steering_wheels = get_steering_wheel()

    brand = request.GET.get("brand", "")
    model = request.GET.get("model", "")
    year = request.GET.get("year", "")
    if year:
        year = int(year)
    city = request.GET.get("city", "")

    body_type = request.GET.get("body_type", "")
    engine_volume = request.GET.get("engine", "")

    if engine_volume:
        engine_volume = float(engine_volume)

    mileage = request.GET.get("mileage", "")

    if mileage:
        mileage = int(mileage)
    else:
        mileage = None
    gear_type = request.GET.get("gear_type", "")

    steering_wheel = request.GET.get("steering_wheel", "")
    color = request.GET.get("color", "")
    wheel_drive = request.GET.get("wheel_drive", "")
    clear = request.GET.get("clear", "")

    fuel_type = request.GET.get("fuel_type", "")

    params = {
        "brand": brand,
        "model": model,
        "year": year,
        "city": city,
        "body": body_type,
        "engine_volume": engine_volume,
        "mileage": mileage,
        "gear_type": gear_type,
        "steering_wheel": steering_wheel,
        "color": color,
        "wheel_drive": wheel_drive,
        "clearenced": clear,
        "fuel_type": fuel_type,
    }

    arr = [
        3434,
        brand,
        model,
        year,
        city,
        body_type,
        engine_volume,
        mileage,
        gear_type,
        steering_wheel,
        color,
        wheel_drive,
        clear,
        0,
        500000,
        fuel_type,
        0,
    ]

    pred_price = None
    if all(v is not None for v in arr):
        pred_price = predict(arr)

    context = {
        "brands": brands,
        "body_types": body_types,
        "fuel_types": fuel_types,
        "wheel_drives": wheel_drives,
        "colors": colors,
        "cities": cities,
        "attributes": attributes,
        "params": params,
        "prediction": pred_price,
        "gear_types": gear_types,
        "steering_wheels": steering_wheels,
    }
    return render(request, "car/predict_car.html", context=context)


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
