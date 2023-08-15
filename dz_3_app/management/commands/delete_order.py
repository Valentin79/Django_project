from django.core.management.base import BaseCommand
from dz_3_app.models import Orders


class Command(BaseCommand):
    help = 'Delete order'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Order ID')

    def handle(self, *args, **options):
        pk = options.get('pk')
        order = Orders.objects.filter(pk=pk).first()
        order.delete()
        self.stdout.write(f'{order}')