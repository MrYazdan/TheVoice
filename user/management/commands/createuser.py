from django.core.management import BaseCommand, CommandError
from ...models import User


class Command(BaseCommand):
    help = "Create user (candidate) by phonenumber and password"

    def add_arguments(self, parser):
        parser.add_argument('user_phone', metavar='UserPhoneNumber',
                            help="User Phone number", type=str)
        parser.add_argument('user_password', metavar='UserPassword',
                            help="User Password", type=str)

    def handle(self, *args, **options):
        user_phone = options['user_phone']
        user_password = options['user_password']

        try:
            user = User.objects.create_user(phone=user_phone, password=user_password)
            self.stdout.write(self.style.SUCCESS(f'User (candidates) : {user.phone}  created!'))
        except Exception as e:
            raise CommandError(e)
