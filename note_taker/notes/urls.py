from django.urls import path 

from . import views

app_name = "notes"


urlpatterns = [
    path('notes/', views.notes_list, name='note_list'),
    path('add/note/', views.add_note, name='add_note'),
    path('edit/note/<int:note_id>/', views.update_note, name='update_note'),
    path('note/<int:note_pk>/', views.note_detail, name='note_detail'),
    path('confirm-delete/<int:note_pk>/', views.confirm_delete, name='confirm_delete'),
    path('delete-note/<int:note_id>/', views.delete_note, name='delete_note'),
]