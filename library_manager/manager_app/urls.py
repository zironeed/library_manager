from django.urls import path

from manager_app.views import BookListView, BookRetrieveView, BookUpdateView, BookCreateView, BookDestroyView
from manager_app.apps import ManagerappConfig

app_name = ManagerappConfig.name

urlpatterns = [
    path('book/create/', BookCreateView.as_view(), name='book_create'),
    path('book/list/', BookListView.as_view(), name='book_list'),
    path('book/retrieve/<int:pk>/', BookRetrieveView.as_view(), name='book_retrieve'),
    path('book/update/<int:pk>/', BookUpdateView.as_view(), name='book_update'),
    path('book/destroy/<int:pk>/', BookDestroyView.as_view(), name='book_destroy'),
]
