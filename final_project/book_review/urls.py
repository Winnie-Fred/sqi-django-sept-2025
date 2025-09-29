from django.urls import path

from . import views

app_name = 'book_review'

urlpatterns = [
    path('', views.home, name='home'),
    path('books/all/', views.all_books, name='all_books'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
]