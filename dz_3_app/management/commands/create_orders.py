from datetime import date, datetime
from django.core.management.base import BaseCommand
from dz_3_app.models import Order, User, Goods
from random import randint

ORDERS = 20


class Command(BaseCommand):
    help = 'Fill table fake data'

    def handle(self, *args, **options):
        for _ in range(1, ORDERS):
            user = User.objects.filter(pk=(randint(1, 5))).first()
            goods = Goods.objects.filter(pk=(randint(1, 10))).first()
            # print(user)
            # print(goods)
            if user and goods:
                if goods.quantity > 0:
                    order_quantity = randint(1, goods.quantity)
                    amount = goods.price * order_quantity
                    # print(f'{goods.price} * {order_quantity} = {goods.price * order_quantity}')
                    order = Order(
                        user_ID=user,
                        goods_ID=goods,
                        quantity=order_quantity,
                        amount=amount,
                        creation_date=datetime.now()
                    )
                    order.save()
                else:
                    print('Товара нет в наличии')
            else:
                print('Не найдено')
