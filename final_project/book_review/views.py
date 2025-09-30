from functools import wraps

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied

from .models import Book, Review
from .forms import ReviewForm

def user_is_review_author(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        review_id = kwargs.get("review_id")
        review = get_object_or_404(Review, pk=review_id)

        if review.added_by != request.user:
            messages.error(request, "You need to be logged in to perform that action.")
            return redirect("accounts:log_in")
        return view_func(request, *args, **kwargs)
    return _wrapped_view

# Create your views here.
def home(request):
    return render(request, "books/home.html")

def all_books(request):
    return render(request, "books/all-books.html", {"books": Book.objects.all()})

def book_detail(request, book_id):
    form = ReviewForm()
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "You need to be logged in to perform that action.")
            return redirect("accounts:log_in")
        
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.added_by = request.user
            review.save()
            return redirect(request.path)
    context = {"book": book, 'form': form}
    return render(request, "books/book-detail.html", context)

@login_required
@user_is_review_author
def edit_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if not review.can_still_be_edited:
        messages.error(request, "You can no longer edit this review")
        return redirect("book_review:book_detail", book_id=review.book.id)
    
    form = ReviewForm(instance=review)
    if request.method == "POST":
  
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("book_review:book_detail", book_id=review.book.pk)
    context = {"review": review, 'form': form}
    return render(request, "reviews/edit-review.html", context)

@login_required
@user_is_review_author
def confirm_delete(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, "reviews/confirm-delete-review.html", {"review": review})

@login_required
@user_is_review_author
def delete_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    if request.method == "POST":
        review.delete()
    return redirect('book_review:book_detail', book_id=review.book.id)
