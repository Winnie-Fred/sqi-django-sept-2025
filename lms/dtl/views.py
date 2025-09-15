from django.shortcuts import render, HttpResponse, get_object_or_404
from django.utils import timezone
from django.http import Http404

from authors.models import Author
from library.models import Book

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



# MVT - Model - View - Template

def models_demo(request):
    all_the_authors = Author.objects.all()
    all_books = Book.objects.all()
    # all_authors_desc = Author.objects.order_by("-first_name")
    # all_authors_desc = all_the_authors.order_by("-first_name")
    all_authors_desc = Author.objects.all().order_by("-first_name")
    # first_author = Author.objects.first()
    first_author = Author.objects.get(pk=1)
    try:
        nonexistent_author = Author.objects.get(pk=100)
    except Author.DoesNotExist:
        nonexistent_author = None
    # try:
    #     nonexistent_author = Author.objects.get(pk=100)
    # except Author.DoesNotExist:
    #     raise Http404("Author does not exist")
    
    # nonexistent_author = get_object_or_404(Author, pk=100)

    authors_ordered_by_birthdate = Author.objects.order_by('-birth_date')
    
    # books_published_after_2001 = Book.objects.filter(published_on__gt="2001-01-01")
    books_published_after_2001 = Book.objects.filter(published_on__year__gt=2001)

    paul = Author.objects.get(pk=2)

    context = {
        'all_authors': all_the_authors,
        'all_the_books': all_books,
        'authors_desc': all_authors_desc,
        'first_author': first_author,
        'nonexistent_author': nonexistent_author,
        'authors_ordered_by_birthdate': authors_ordered_by_birthdate,
        'books_published_after_2001': books_published_after_2001,
        'paul': paul

    }
    return render(request, "dtl/models-demo.html", context)