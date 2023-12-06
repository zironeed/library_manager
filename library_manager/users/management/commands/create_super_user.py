from django.core.management import BaseCommand
from users.models import User
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """A command for easily creating a user and a superuser"""
    def handle(self, *args, **options):
        check_admin = User.objects.filter(email='admin@gmail.com')

        if check_admin:
            logger.info(f"""
*********************
We already have admin!
*********************""")
            return 0

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
