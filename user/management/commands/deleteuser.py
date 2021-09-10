from django.core.management import BaseCommand, CommandError
from ...models import User


class Command(BaseCommand):
    help = "Delete users by phone numbers"

    def add_arguments(self, parser):
        parser.add_argument('phone_numbers', nargs='+', type=str, help='User Phone Numbers')

    def handle(self, *args, **kwargs):
        users_phones = kwargs['phone_numbers']

        for phone in users_phones:
            try:
                user = User.objects.get(phone=phone)
                user.delete()
                self.stdout.write(self.style.SUCCESS(f'User {user.phone} deleted with success!'))
            except User.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'User with id {phone} does not exist.'))
