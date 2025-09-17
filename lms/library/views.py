from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

from .models import Book
from library.models import Author
from .forms import BookForm

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


def create_book(request):
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()       
            return redirect('library:book_list')

    context = {
        'form': form
    }
    return render(request, "library/create-book.html", context)