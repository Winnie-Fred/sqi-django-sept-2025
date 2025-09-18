from django import forms

from .models import Book
from authors.models import Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "number_of_pages", "published_on", "cover_image"]

    # def clean(self):
    #     cleaned_data = super().clean()
    #     title = cleaned_data.get("title")
    #     published_on = cleaned_data.get("published_on")

    #     # Example: forbid books published before 1900
    #     if published_on and published_on.year < 1900:
    #         raise forms.ValidationError("Books published before 1900 are not allowed.")

    #     return cleaned_data


class BookManualForm(forms.Form):
    title = forms.CharField(max_length=255)
    author = forms.ModelChoiceField(queryset=Author.objects.all()) 
    number_of_pages = forms.IntegerField(min_value=1)
    published_on = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    cover_image = forms.ImageField(required=False)