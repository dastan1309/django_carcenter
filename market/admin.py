from django.contrib import admin

from market.models import Car, Order, Purchased, Payment

admin.site.register(Car)
admin.site.register(Order)
admin.site.register(Purchased)
admin.site.register(Payment)