from django import forms

from .models import Note, Category

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'category']


class SearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=False)
    

class FilterForm(forms.Form):
    category = forms.ChoiceField(choices=Category.choices, initial=Category.WORK, required=False)