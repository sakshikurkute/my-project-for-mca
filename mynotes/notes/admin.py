from django.contrib import admin

from .models import Note, ContactMessage


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'note_type',
        'uploaded_at'
    )

    list_filter = (
        'note_type',
        'uploaded_at'
    )

    search_fields = (
        'title',
        'description'
    )


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'created_at'
    )

    search_fields = (
        'name',
        'email'
    )
