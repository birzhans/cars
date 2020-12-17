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
    brands = [
        "Nissan",
        "Mitsubishi",
        "ВАЗ (Lada)",
        "Porsche",
        "JAC",
        "Toyota",
        "Chevrolet",
        "Volkswagen",
        "Mercedes-Benz",
        "Ford",
        "Audi",
        "Suzuki",
        "Peugeot",
        "BMW",
        "Hyundai",
        "Kia",
        "Opel",
        "Lexus",
        "Hummer",
        "Land Rover",
        "Daewoo",
        "Cadillac",
        "ГАЗ",
        "Renault",
        "Subaru",
        "Dodge",
        "Lifan",
        "УАЗ",
        "Infiniti",
        "GMC",
        "ИЖ",
        "Skoda",
        "Mazda",
        "Ravon",
        "Honda",
        "Foton",
        "Jaguar",
        "Tesla",
        "Rover",
        "Mini",
        "SsangYong",
        "Geely",
        "Great Wall",
        "Volvo",
        "Chrysler",
        "Lincoln",
        "Mercedes-Maybach",
        "Fiat",
        "Jeep",
        "Isuzu",
        "Москвич",
        "Renault Samsung",
        "Maserati",
        "Citroen",
        "Chery",
        "Bentley",
        "ЗАЗ",
        "Datsun",
        "ТагАЗ",
        "FAW",
        "Scion",
        "BYD",
        "Seat",
        "Changan",
        "Genesis",
        "Acura",
        "Saab",
        "Lancia",
        "Haima",
        "РАФ",
        "MG",
        "Wuling",
        "Pontiac",
        "ZX",
        "Ретро-автомобили",
        "DongFeng",
        "Maybach",
        "Mercury",
        "Bugatti",
        "Daihatsu",
        "Rolls-Royce",
        "Saturn",
        "BAIC",
        "ЛуАЗ",
        "Alfa Romeo",
        "Tianye",
    ]
    brand = request.GET.get("brand", "")
    year_from = request.GET.get("yearFrom", "")
    year_to = request.GET.get("yearTo", "")
    price_from = request.GET.get("priceFrom", "")
    price_to = request.GET.get("priceTo", "")

    cars = Car.objects.all()

    if brand:
        cars = cars.filter(brand=brand)

    if year_from and year_to:
        cars = cars.filter(year__lte=int(year_to)).filter(year__gte=int(year_from))
    elif year_from:
        cars = cars.filter(year__gte=int(year_from))
    elif year_to:
        cars = cars.filter(year__lte=int(year_to))

    if price_from and price_to:
        cars = cars.filter(price__lte=int(price_to)).filter(year__gte=int(price_from))
    elif price_from:
        cars = cars.filter(price__gte=int(price_from))
    elif price_to:
        cars = cars.filter(price__lte=int(price_to))

    if cars.count() > 20:
        cars = cars[:20]

    return render(
        request, "car/find_car.html", context={"cars": cars, "brands": brands}
    )


def predict_car(request):
    return render(request, "car/predict_car.html")


def analysis(request):
    return render(request, "car/predict_car.html")
