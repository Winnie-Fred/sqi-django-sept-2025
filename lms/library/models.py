from django.db import models

from authors.models import Author

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    number_of_pages = models.PositiveIntegerField()
    published_on = models.DateTimeField()