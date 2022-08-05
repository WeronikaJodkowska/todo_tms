from django.shortcuts import render, redirect

from notes.forms import AddNoteForm
from notes.models import Note


def index(request):
    notes = Note.objects.all()
    if request.method == "POST":
        form = AddNoteForm(request.POST)
        if form.is_valid():
            Note.objects.create(
                author=request.user, title=form.cleaned_data["title"], text=form.cleaned_data["text"]
            )
            return redirect("index")
    else:
        form = AddNoteForm()
    return render(request, "note_list.html", {"notes": notes, "form": form})
