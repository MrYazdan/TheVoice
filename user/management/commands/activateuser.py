from django.core.management import BaseCommand, CommandError
from ...models import User


class Command(BaseCommand):
    help = "Activate user by phonenumber"
    u: User = User

    def add_arguments(self, parser):
        parser.add_argument('user_phone', metavar='UserPhoneNumber',
                            help="User Phone number", type=str)

    def handle(self, *args, **options):
        user_phone = options['user_phone']
        try:
            self.u = User.objects.get(phone=user_phone)
            self.u.is_active = True
            self.u.save()
            self.stdout.write(self.style.SUCCESS(f'User : {self.u.phone} activated!'))
        except Exception as e:
            raise CommandError(e)
