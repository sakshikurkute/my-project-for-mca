from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Property, Service, Gallery, Inquiry  # Ensure Property is imported here

def home(request):
    properties = Property.objects.all()  # This line should now work as Property is imported
    return render(request, 'website/home.html', {'properties': properties})

def services(request):
    services = Service.objects.all()
    return render(request, 'website/services.html', {'services': services})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        Inquiry.objects.create(name=name, email=email, phone=phone, message=message)
    return render(request, 'website/contact.html')

def gallery(request):
    gallery = Gallery.objects.all()
    return render(request, 'website/gallery.html', {'gallery': gallery})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        # Check if the user exists and if they are an admin (is_staff=True)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard')  # Redirect to the admin dashboard
        else:
            error = "Invalid login credentials or insufficient privileges"
            return render(request, 'login.html', {'error': error})
    
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            error = "Passwords do not match"
            return render(request, 'signup.html', {'error': error})

        # Manually create the user
        user = UserCreationForm({'username': username, 'email': email, 'password1': password, 'password2': confirm_password})
        
        if user.is_valid():
            user.save()

            # Set the user as an admin (is_staff) after successful registration
            created_user = authenticate(request, username=username, password=password)
            if created_user is not None:
                created_user.is_staff = True  # Assigning admin privileges
                created_user.save()  # Save the user with admin privileges

            return redirect('login')  # Redirect to login page after successful signup
        else:
            return render(request, 'signup.html', {'error': "Signup failed. Please try again."})
    
    return render(request, 'signup.html')


from django.shortcuts import render
from .models import WebsiteInquiry

def dashboard(request):
    inquiries = WebsiteInquiry.objects.all()  # Fetching all inquiries
    return render(request, 'website/dashboard.html', {'user': request.user, 'inquiries': inquiries})



def admin_logout(request):
    logout(request)
    return redirect('login')

