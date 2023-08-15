from datetime import date, datetime
from django.core.management.base import BaseCommand
from dz_3_app.models import User, Goods
from random import randint


USERS = 5
GOODS = 10



class Command(BaseCommand):
    help = 'Fill table fake data'

    def handle(self, *args, **options):
        for i in range(1, USERS+1):
            user = User(
                name=f"User{i}",
                email=f"mail{i}@mail.com",
                phone=f"{i}{i}{i}{i}{i}",
                address=f"address{i}",
                birthday=date.today()
            )
            user.save()

        for i in range(1, GOODS+1):
            goods = Goods(
                title=f'title{i}',
                description=f'description{i}',
                price=randint(10, 1000),
                quantity=randint(0, 100),
                added=datetime.now()
            )
            goods.save()

