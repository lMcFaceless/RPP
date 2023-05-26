from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Seller(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Dish(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Product(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Order(models.Model):
    number = models.IntegerField()
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    seller = models.OneToOneField(Seller, on_delete=models.CASCADE)
    dish = models.ManyToManyField(Dish)
