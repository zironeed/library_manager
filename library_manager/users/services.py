from django.core.mail import send_mail as sm


def send_mail(email):
    res = sm(
        subject='Добро пожаловать!',
        message='Благодарим вас за регистрацию на портале нашей библиотеки!',
        from_email='better@library.ru',
        recipient_list=[email],
    )

    print(f'mail sent to {email}')
