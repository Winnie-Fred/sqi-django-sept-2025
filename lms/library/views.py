from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Book

# Create your views here.

def home(request):
    return render(request, "library/home.html")

def book_list(request):
    return render(request, "library/book-list.html", {"all_books": Book.objects.all()})

# django template language - DTL

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    # try:
    #     book = Book.objects.get(pk=book_id)
    # except Book.DoesNotExist:
    #     raise Http404("Book does not exist")
    return render(request, "library/book-detail.html", {"book": book})