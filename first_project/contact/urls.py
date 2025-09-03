from django.urls import path

from . import views

urlpatterns = [
    path('phone-us', views.phone_us, name='phone_us'),
]