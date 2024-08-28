from django.core.management.base import BaseCommand
# from booking.utils import check_and_expire_bookings  # Adjust the import path as needed
from booking.views import check_and_expire_bookings

class Command(BaseCommand):
    help = 'Check and expire expired bookings'

    def handle(self, *args, **options):
        check_and_expire_bookings()
        self.stdout.write(self.style.SUCCESS('Successfully checked and expired bookings'))
