from rest_framework import serializers
from manager_app.models import Book


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', 'author', 'publish_year', 'isbn',)
