from django.db import models
from manager_app.custom_validators import publish_year_validator, isbn_validator


class Book(models.Model):
    title = models.CharField(max_length=150, verbose_name='book_title')
    author = models.CharField(max_length=200, verbose_name='book_author')
    publish_year = models.IntegerField(verbose_name='book_publish_year', validators=[publish_year_validator])
    isbn = models.IntegerField(verbose_name='book_isbn', validators=[isbn_validator])

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return f"""Title: {self.title}
        Author: {self.author}"""
