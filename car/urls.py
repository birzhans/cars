from django.urls import include, path
from .views import index, car_detail

urlpatterns = [
    path("", index, name="car_index_path"),
    path("<str:id>/", car_detail, name="car_detail_url"),
]
