from django import forms
from .models import Note, ContactMessage


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = [
            'title',
            'description',
            'note_type',
            'file',
            'text_content'
        ]

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter note title'
                }
            ),

            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter description',
                    'rows': 4
                }
            ),

            'note_type': forms.Select(
                attrs={
                    'class': 'form-control'
                }
            ),

            'file': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'text_content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Enter your note',
                    'rows': 8
                }
            ),
        }


class ContactForm(forms.ModelForm):

    class Meta:
        model = ContactMessage

        fields = [
            'name',
            'email',
            'message'
        ]

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your Name'
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your Email'
                }
            ),

            'message': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Your Message',
                    'rows': 5
                }
            ),
        }
