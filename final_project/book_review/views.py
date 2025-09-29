from django.shortcuts import render, get_object_or_404

from .models import Author, Book

# Create your views here.
def home(request):
    return render(request, "books/home.html")

def all_books(request):
    return render(request, "books/all-books.html", {"books": Book.objects.all()})

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "books/book-detail.html", {"book": book})