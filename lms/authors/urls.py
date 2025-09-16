from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('', views.all_authors, name='all_authors'),
    path('book-signings/', views.book_signings, name='book_signings'),
    path('author/<str:author_pk>/', views.author_detail, name='author_detail'),
]