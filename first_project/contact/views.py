from django.shortcuts import render, HttpResponse

# Create your views here.

# MVT - MODEL-VIEW-TEMPLATE
# MVC - MODEL-VIEW-CONTROLLER


def phone_us(request):
    return HttpResponse("Phone us: '+2349030556549'")
