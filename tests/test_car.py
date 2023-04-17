from django.test import TestCase
from market.models import Car, Purchased, Order


class PurchaseTest(TestCase):
    def setUp(self):
        Car.objects.create(name="Audi A6")
        Car.objects.create(name="Audi A7")
        Car.objects.create(name="Audi A8")

    def test_car_count(self):
        self.assertEqual(Car.objects.all().count(), 3)
        car = Car.objects.get(name="Audi A7")
        assert car.name == "Audi A7"


    def test_cars_left_function(self):
        car = Car.objects.get(name="Audi A6")
        # buy 3 cars
        Purchased.objects.create(car=car, count=3)
        # sell 1 car
        Order.objects.create(car=car)
        # we should have 2 cars left
        self.assertEqual(car.cars_left(), 2)
        car = Car.objects.get(name="Audi A7")
        self.assertEqual(car.cars_left(), 0)

