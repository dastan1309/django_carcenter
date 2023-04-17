import random

from django.http import HttpRequest, HttpResponse


def show_weather(request: HttpRequest)->HttpResponse:
    temp = random.randint(-40,40)
    feel= 'Ok'
    if temp>20:
        feel = "hot"
    if temp < 0 :
        feel = "cold"
    if temp < -10:
        feel = "very cold"
    return HttpResponse(f"Today: {temp} , grad celsius, it is {feel}")