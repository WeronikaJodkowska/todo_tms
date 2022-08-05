from django.contrib import admin

from notes.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("author", "title", "created_at")
    fields = ("author", "title", "text")
    search_fields = ("title", "text")
    raw_id_fields = ("author", )
