from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from .models import Contact

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class CustomUserLoginForm(AuthenticationForm):
    pass

from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'contact', 'email', 'subject', 'message', 'location']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }
