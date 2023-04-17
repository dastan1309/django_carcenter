from typing import List, Any

from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import path

from djangoProject2.views_name import name
from view_weather import show_weather
#from views_audi import audi_purchase
from market.views import show_cars, audi_purchase, payment


def hello_world(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',hello_world),
    path('weather', show_weather),
    path('audi',show_cars),
    path('buy_car/<int:id_>/', audi_purchase),
    path('name', name),
    path('payment/<int:id_>', payment),
]
