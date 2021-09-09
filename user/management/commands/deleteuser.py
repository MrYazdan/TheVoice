from django.core.management import BaseCommand, CommandError
from ...models import User


class Command(BaseCommand):
    help = "Delete users by id"

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        users_ids = kwargs['user_id']

        for user_id in users_ids:
            try:
                user = User.objects.get(pk=user_id)
                user.delete()
                self.stdout.write(self.style.SUCCESS(f'User {user.username} deleted with success!'))
            except User.DoesNotExist:
                self.stdout.write(self.style.WARNING(f'User with id {user_id} does not exist.'))
