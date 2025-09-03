from django.urls import path

from . import views

urlpatterns = [
    path('events/', views.community_events, name='community_events'),
]