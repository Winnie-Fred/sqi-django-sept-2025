from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.book_list, name='book_list'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
    path('add/book/', views.create_book, name='create_book'),
    path('add/book/manually-rendered/', views.create_book_manually_rendered, name='create_book_manually_rendered'),
    path('add/book/django-manual-form/', views.create_book_django_manual_form, name='create_book_django_manual_form'),
]