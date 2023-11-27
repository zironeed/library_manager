from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True, verbose_name='user_name')
    email = models.EmailField(max_length=150, unique=True, verbose_name='user_email')
    registration_date = models.DateField(auto_now_add=True, verbose_name='user_registration_date')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return f'{self.email}; {self.registration_date}'
