from celery import shared_task
from users.services import send_mail


@shared_task
def send_letter(email):
    """
    Отправка приветственного письма пользователю
    """
    send_mail(email)
