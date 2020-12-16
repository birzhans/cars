from django.urls import include, path
from .views import index, car_detail

urlpatterns = [
    path("", index),
    path("<str:id>/", car_detail, name="car_detail_url"),
]
