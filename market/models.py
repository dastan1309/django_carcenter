from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=255, blank=False, null=True)
    available = models.IntegerField(default=0)
    image = models.CharField(max_length=1000, blank=True, default="")
    price = models.IntegerField(default=0)
    description = models.CharField(max_length= 10000, null=True, default="Все подробности на Сайте")



    def __str__(self):
        return f"{self.name}, available{self.available}"


    def cars_left(self) -> int:
        ordered = Order.objects.filter(car=self).count()
        purchased = Purchased.objects.filter(car=self).count()
        return purchased - ordered


class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255)
    status = models.CharField(max_length=100, default="created")


    def __str__(self):
        return f"{self.car}, {self.name}, phone: {self.phone}, status: {self.status} "


class Purchased(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.car}, purchased at: {self.date}"


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    credit_card = models.CharField(max_length=255, blank=True,null=True)


    def __str__(self):
        return f"{self.order}, amount:{self.amount}, date: {self.date}"




