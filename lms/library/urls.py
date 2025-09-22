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
    path('update/book/model-form/<int:book_pk>/', views.update_book_model_form, name='update_book_model_form'),
    path('update/book/manual-form/<int:pk>/', views.update_book_manual_form, name='update_book_manual_form'),
    path('confirm-delete/<int:pk>/', views.confirm_delete, name='confirm_delete'),
    path('delete-book/<int:book_pk>/', views.delete_book, name='delete_book'),
]