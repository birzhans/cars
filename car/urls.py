from django.urls import include, path
from .views import index, find_car, analysis, predict_car, car_detail

urlpatterns = [
    path("", index, name="car_index_url"),
    path("find/", find_car, name="find_car_url"),
    path("analysis/", analysis, name="analysis_url"),
    path("predict-price/", predict_car, name="predict_price_url"),
    path("<str:id>/", car_detail, name="car_detail_url"),
]
