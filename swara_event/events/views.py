from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm

def home(request):
    events = Event.objects.all()
    return render(request, 'events/home.html', {'events': events})


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'events/add_event.html', {'form': form})
    