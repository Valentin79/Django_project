from django.core.management.base import BaseCommand
from dz_3_app.models import Goods


class Command(BaseCommand):
    help = 'Change quantity goods'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Goods ID')
        parser.add_argument('quantity', type=int, help='goods quantity')

    def handle(self, *args, **options):
        pk = options.get('pk')
        quantity = options.get('quantity')
        goods = Goods.objects.filter(pk=pk).first()
        if goods:
            goods.quantity = quantity
            goods.save()
        self.stdout.write(f'{goods}')