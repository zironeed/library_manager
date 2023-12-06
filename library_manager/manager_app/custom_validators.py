from rest_framework import validators


def publish_year_validator(year):
    """
    Валидация года выпуска книги
    """
    if year > 2023 or year < 1800:
        raise validators.ValidationError('Enter the correct publication year')


def isbn_validator(isbn):
    """
    Валидация ISBN-номера книги
    """
    if len(str(isbn)) != 10 and len(str(isbn)) != 13:
        raise validators.ValidationError('Enter the correct ISBN')
