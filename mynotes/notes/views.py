from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test

from .models import Note, ContactMessage
from .forms import NoteForm, ContactForm


def home(request):
    latest_notes = Note.objects.order_by('-uploaded_at')[:6]

    return render(
        request,
        'notes/home.html',
        {
            'latest_notes': latest_notes
        }
    )


def notes_list(request):
    all_notes = Note.objects.order_by('-uploaded_at')

    return render(
        request,
        'notes/notes.html',
        {
            'notes': all_notes
        }
    )


def upload_note(request):

    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Your note has been uploaded successfully!'
            )
            return redirect('notes')

    else:
        form = NoteForm()

    return render(
        request,
        'notes/upload.html',
        {
            'form': form
        }
    )


def about(request):
    return render(request, 'notes/about.html')


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Your message has been sent successfully!'
            )

            return redirect('contact')

    else:
        form = ContactForm()

    return render(
        request,
        'notes/contact.html',
        {
            'form': form
        }
    )


def admin_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard')

        messages.error(
            request,
            'Invalid admin username or password.'
        )

    return render(
        request,
        'notes/admin_login.html'
    )


@user_passes_test(lambda user: user.is_staff)
def dashboard(request):

    all_notes = Note.objects.all().order_by('-uploaded_at')
    contacts = ContactMessage.objects.all().order_by('-created_at')

    context = {
        'notes': all_notes,
        'contacts': contacts,
        'total_notes': Note.objects.count(),
        'total_contacts': ContactMessage.objects.count(),
        'pdf_count': Note.objects.filter(note_type='pdf').count(),
        'image_count': Note.objects.filter(note_type='image').count(),
        'text_count': Note.objects.filter(note_type='text').count(),
    }

    return render(
        request,
        'notes/dashboard.html',
        context
    )


def admin_logout(request):
    logout(request)
    return redirect('admin_login')
