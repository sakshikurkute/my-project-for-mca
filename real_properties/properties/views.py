from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, CustomUserLoginForm
from .forms import ContactForm
from .models import Contact
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to dashboard after successful login
            return redirect('dashboard')  # Ensure 'dashboard' URL is defined in your URLs
    else:
        form = CustomUserLoginForm()
    return render(request, 'login.html', {'form': form})

def dashboard(request):
    if not request.user.is_authenticated:  # Ensure user is logged in
        return redirect('login')  # Redirect to login page if not authenticated
    contacts = Contact.objects.all()
    return render(request, 'dashboard.html',{'contacts': contacts})  # Render the dashboard template

def user_logout(request):
    logout(request)
    return redirect('login')



def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the dashboard after form submission
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  # Redirect after successful submission
    else:
        form = ContactForm()
    return render(request, 'contact_us.html', {'form': form})
