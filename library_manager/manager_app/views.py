from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from manager_app.serializers import BookSerializer

from manager_app.models import Book


class BookCreateView(CreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookRetrieveView(RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookListView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookUpdateView(UpdateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookDestroyView(DestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
