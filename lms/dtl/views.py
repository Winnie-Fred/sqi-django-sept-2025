from django.shortcuts import render, HttpResponse

from django.utils import timezone

# Create your views here.
def django_template_language(request):
    context = {
        "my_name": "Lekan",
        "age": 20,
        "hobbies": ["playing", "eating", "coding", "sports", "cycling", "listening to music", "cooking"],
        "weight": 73,
        "is_logged_in": False,
        "notifications": ["dannify started following you", "someone just liked your post", "You have 3 new messages"],
        "profile": {
            "gender": "Male",
            "location": "Ibadan",
            "is_married": False,
            "address": {
                "house number": "No 16",
                "state": "Oyo",
                "city": "Ibadan",
                "lga": "Ibadan North",
                "zip code": "230896",
                "phone_number": "08166243885",
            }
        },
        "today": timezone.now()
    }
    return render(request, "dtl/dtl.html", context)


def home(request):
    return HttpResponse('<h1>This is the DTL home page</h1>')