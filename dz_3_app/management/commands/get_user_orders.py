from django.core.management.base import BaseCommand
from dz_3_app.models import User, Order


class Command(BaseCommand):
    help = 'User info'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **options):
        pk = options.get('pk')
        user = User.objects.filter(pk=pk).first()
        orders = Order.objects.filter(user_ID=user)
        print(user)
        for order in orders:
            item = order.goods_ID
            print(f'Товар: {item}')
            print(f'Количество: {order.quantity}, Сумма: {order.amount}, Дата: {order.creation_date}')
        # order_list = '\n'.join(str(order.goods_ID) for order in orders)
        # self.stdout.write(f'{user}\n{order_list}')