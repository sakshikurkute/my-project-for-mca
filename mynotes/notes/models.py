from django.db import models


class Note(models.Model):
    NOTE_TYPES = (
        ('pdf', 'PDF'),
        ('image', 'Image'),
        ('text', 'Text'),
    )

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    note_type = models.CharField(max_length=10, choices=NOTE_TYPES)

    file = models.FileField(
        upload_to='notes/',
        blank=True,
        null=True
    )

    text_content = models.TextField(
        blank=True,
        null=True
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
