from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator
from django.core.exceptions import ValidationError

from authors.models import Author


def validate_title_has_no_special_chars(value: str):
    if not all(char.isalpha() or char.isspace() for char in value):
        raise ValidationError("Title can only contain alphabets and spaces!")

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255, validators=[MinLengthValidator(10), validate_title_has_no_special_chars])
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    number_of_pages = models.PositiveIntegerField(validators=[MaxValueValidator(7000)])
    published_on = models.DateTimeField()
    cover_image = models.ImageField(upload_to="cover_images/", null=True, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"