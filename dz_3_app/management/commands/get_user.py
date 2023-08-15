from django.core.management.base import BaseCommand
from dz_3_app.models import User


class Command(BaseCommand):
    help = 'User info'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **options):
        pk = options.get('pk')
        user = User.objects.filter(pk=pk).first()
        self.stdout.write(f'{user}')