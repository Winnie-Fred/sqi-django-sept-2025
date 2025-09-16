from django.shortcuts import render, get_object_or_404

from .models import Author

# Create your views here.

def all_authors(request):
    return render(request, "authors/all-authors.html", {"all_authors": Author.objects.all()})

def book_signings(request):
    return render(request, "authors/book-signings.html")


def author_detail(request, author_pk):
    author = get_object_or_404(Author, pk=author_pk)
    return render(request, "authors/author-detail.html", {"author": author})