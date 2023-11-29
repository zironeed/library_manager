from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """A command for easily creating a user and a superuser"""
    def handle(self, *args, **options):
        check_admin = User.objects.filter(email='admin@gmail.com')

        if check_admin:
            return 'We already have admin!'

        admin = User.objects.create(
            username='admin',
            email='admin@gmail.com',
            first_name='admin',
            last_name='admin',
            is_active=True,
            is_staff=True,
            is_superuser=True
        )

        admin.set_password('12345')
        admin.save()
