from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Note
from .forms import NoteForm, SearchForm, FilterForm

# Create your views here.
def notes_list(request):
    notes = Note.objects.all()

    search_form = SearchForm(request.GET)

    if search_form.is_valid():
        query = search_form.cleaned_data.get('query')
        if query:
            notes = Note.objects.all().filter(Q(title__icontains=query) | Q(content__icontains=query))

    filter_form = FilterForm(request.GET)
    if filter_form.is_valid():
        category = filter_form.cleaned_data.get('category')
        if category:
            notes = notes.filter(category=category)
    context = {
        "notes": notes, 
        'search_form': search_form,
        'filter_form': filter_form
    }
    return render(request, "notes/note-list.html", context)


def note_detail(request, note_pk):
    note = get_object_or_404(Note, pk=note_pk)
    return render(request, "notes/note.html", {'note': note})


@login_required
def add_note(request):
    form = NoteForm()
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.added_by = request.user
            note.save()
            return redirect("notes:note_list")
    context = {'form': form}
    return render(request, "notes/add-note.html", context)


@login_required
def update_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.user != note.added_by:
        messages.error(request, "You do not have permission to perform that action")
        return redirect("notes:note_list")
    form = NoteForm(instance=note)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("notes:note_detail", note_pk=note_id)
    context = {'note': note, 'form': form}
    return render(request, "notes/edit-note.html", context)

@login_required
def confirm_delete(request, note_pk):
    note = get_object_or_404(Note, pk=note_pk)
    if request.user != note.added_by:
        messages.error(request, "You do not have permission to perform that action")
        return redirect("notes:note_list")
    return render(request, "notes/confirm-delete.html", context={"note": note})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.user != note.added_by:
        messages.error(request, "You do not have permission to perform that action")
        return redirect("notes:note_list")
    if request.method == "POST":
        note.delete()
    return redirect("notes:note_list")