import os

from django.db import models
from django.template.defaultfilters import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField()
    date_of_birth = models.DateField()
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class GenreChoices(models.TextChoices):
    FANTASY = "FTSY", "Fantasy"
    SCI_FI = "SCIFI", "Science Fiction"
    MYSTERY_THRILLER = "MYST_THRILL", "Mystery/Thriller"
    ROMANCE = "ROM", "Romance" 
    HISTORICAL_FICTION = "HIST_FIC", "Historical Fiction"
    HORROR = "HORROR", "Horror"
    DYSTOPIAN = "DYST", "Dystopian"
    ADVENTURE = "ADVN", "Adventure"
    BIO_AUTOBIO = "BIO_AUTOBIO", "Biography/Autobiography"
    SELF_HELP = "SELF_HELP", "Self Help"
    HISTORY = "HIST", "History"
    SCIENCE = "SCI", "Science"
    BUSINESS = "BSNS", "Business"

def book_cover_upload_to(instance, filename):
    _, ext = os.path.splitext(filename)
    return f"book_cover_images/{slugify(instance.title)}{ext}"


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100, choices=GenreChoices.choices, default=GenreChoices.FANTASY)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)
    cover_image = models.ImageField(upload_to=book_cover_upload_to, default="defaults/default-cover.jpg")
    number_of_pages = models.PositiveIntegerField()
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} by {self.author}"
    


class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    content = models.TextField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def can_still_be_edited(self):
        now = timezone.now()
        return now - self.created_at <= timedelta(minutes=5)