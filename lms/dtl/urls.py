from django.urls import path

from . import views

app_name = 'dtl'

urlpatterns = [
    path('demo/', views.django_template_language, name='dtl_demo'),
    path('home/', views.home, name='home'),
]