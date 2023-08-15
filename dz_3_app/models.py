from datetime import datetime
from django.db import models



# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    birthday = models.DateField(default=datetime.now())

    def __str__(self):
        return f'{self.name}, {self.birthday}, {self.phone}'


class Goods(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    added = models.DateField(default=datetime.today())
    image = models.ImageField(default=None)

    def __str__(self):
        return f'{self.title}, {self.price}, {self.description}'


class Order(models.Model):
    user_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    goods_ID = models.ForeignKey(Goods, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    creation_date = models.DateField(default=datetime.now())

    def __str__(self):
        return f'{self.user_ID.name}, {self.goods_ID.title}, {self.amount}'
