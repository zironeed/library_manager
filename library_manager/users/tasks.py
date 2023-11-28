from celery import shared_task
from users.services import send_mail


@shared_task
def send_letter(email):
    send_mail(email)
