from django.urls import path

from . import views

app_name = "portfolio"

urlpatterns = [
    path("services/", views.services, name='services'),
    path("testimonials/", views.testimonials, name='testimonials'),
    path("pricing/", views.pricing, name='pricing'),
    path("case-studies/", views.case_studies, name='case_studies'),
    path("blog/", views.blog, name='blog'),
]