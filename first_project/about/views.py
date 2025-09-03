from django.shortcuts import render, HttpResponse

# Create your views here.
def about_us(request):
    return HttpResponse("<div>Some info about us</div>")