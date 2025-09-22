from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

from .models import Book
from library.models import Author
from .forms import BookForm, BookManualForm

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


def create_book_manually_rendered(request):
    all_authors = Author.objects.all()
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()       
            return redirect('library:book_list')
        else:
            print(form.errors)

    context = {
        'form': form,
        'all_authors': all_authors
    }
    return render(request, "library/create-book-manually-rendered.html", context)


def create_book_django_manual_form(request):
    form = BookManualForm()
    if request.method == "POST":
        form = BookManualForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            # Book.objects.create(
            #     title=cleaned_data.get('title'),
            #     author=cleaned_data.get('author'),
            #     number_of_pages=cleaned_data.get('number_of_pages'),
            #     published_on=cleaned_data.get('published_on'),
            #     cover_image=cleaned_data.get('cover_image')
            # )
            Book.objects.create(**cleaned_data)
            return redirect('library:book_list')


    context = {'form': form}
    return render(request, "library/create-book-django-manual-form.html", context)

def update_book_model_form(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    form = BookForm(instance=book)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)

        if form.is_valid():
            form.save()
            return redirect('library:book_list')

    context = {
        'form': form,
        'book': book,
    }
    return render(request, "library/update-book-model-form.html", context)


def update_book_manual_form(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookManualForm(initial={
        'title': book.title,
        'author': book.author,
        'number_of_pages': book.number_of_pages,
        'published_on': book.published_on,
        'cover_image': book.cover_image,
    })
    if request.method == "POST":
        form = BookManualForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            book.title = cleaned_data.get('title')
            book.author = cleaned_data.get('author')
            book.number_of_pages = cleaned_data.get('number_of_pages')
            book.published_on = cleaned_data.get('published_on')
            book.cover_image = cleaned_data.get('cover_image')
            book.save()
            return redirect('library:book_detail', book_id=pk)
    context = {'form': form, 'book': book}
    return render(request, "library/update-book-django-manual-form.html", context)   


def confirm_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "library/confirm-delete.html", {'book': book})


def delete_book(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    if request.method == "POST":
        book.delete()
    return redirect("library:book_list")
