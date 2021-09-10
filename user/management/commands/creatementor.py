from django.core.management import BaseCommand, CommandError
from ...models import Mentor


class Command(BaseCommand):
    help = "Create mentor by phonenumber and password"

    def add_arguments(self, parser):
        parser.add_argument('user_phone', metavar='UserPhoneNumber',
                            help="User Phone number", type=str)
        parser.add_argument('user_password', metavar='UserPassword',
                            help="User Password", type=str)

    def handle(self, *args, **options):
        user_phone = options['user_phone']
        user_password = options['user_password']

        try:
            user = Mentor.objects.create_user(phone=user_phone, password=user_password)
            self.stdout.write(self.style.SUCCESS(f'Mentor : {user.phone}  created!'))
        except Exception as e:
            raise CommandError(e)
