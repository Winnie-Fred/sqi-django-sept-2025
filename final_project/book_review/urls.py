from django.urls import path

from . import views

app_name = 'book_review'

urlpatterns = [
    path('', views.home, name='home'),
    path('books/all/', views.all_books, name='all_books'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('review/edit/<int:review_id>/', views.edit_review, name='edit_review'),
    path('review/confirm-delete/<int:review_id>/', views.confirm_delete, name='confirm_delete'),
    path('review/delete/<int:review_id>/', views.delete_review, name='delete_review'),
]