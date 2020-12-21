from django.contrib.auth.forms import (
    UserCreationForm,
)
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import (
    reverse_lazy,
)
from django.views.generic import (
    CreateView,
)
from car.models import Car
from .models import Profile

def ProfileView(request):
    user = request.user
    favourite_car = user.favourite.all()
    print(favourite_car)

    template = loader.get_template('user/profile.html')

    context = {
        'favourite_car': favourite_car,
    }

    return HttpResponse(template.render(context, request))

class RegisterView(CreateView):
    template_name = 'user/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy(
        'car_index_url')





