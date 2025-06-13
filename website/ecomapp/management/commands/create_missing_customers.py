from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ecomapp.models import Customer

class Command(BaseCommand):
    help = 'Creates Customer objects for users who don\'t have one'

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        for user in users:
            if not hasattr(user, 'customer'):
                Customer.objects.create(
                    user=user,
                    full_name=user.username,
                    address=''
                )
                self.stdout.write(
                    self.style.SUCCESS(f'Created Customer for user {user.username}')
                ) 