from django.shortcuts import render
from .models import Event, Gallery

def index(request):
    events = Event.objects.all()
    return render(request, 'index.html', {'events': events})

def gallery(request):
    gallery = Gallery.objects.all()
    return render(request, 'gallery.html', {'gallery': gallery})
