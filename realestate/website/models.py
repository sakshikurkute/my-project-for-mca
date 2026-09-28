# models.py
from django.db import models

class Property(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    description = models.TextField()

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery_images/')
    description = models.CharField(max_length=255)

# models.py

from django.db import models

class Inquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)  # Automatically set the timestamp when the inquiry is created

    def __str__(self):
        return f"Inquiry from {self.name}"

from django.db import models

class WebsiteInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)  # Ensure this field exists

    def __str__(self):
        return self.name
