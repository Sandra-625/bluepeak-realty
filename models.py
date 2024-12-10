from django.db import models
from django.contrib.auth.models import User



class Property(models.Model):
    PROPERTY_TYPES = [
        ('house', 'House'),
        ('apartment', 'Apartment'),
        ('condo', 'Condominium'),
        ('land', 'Land'),
    ]

    STATUS_CHOICES = [
        ('sale', 'For Sale'),
        ('rent', 'For Rent'),
        ('sold', 'Sold'),
    ]

    title = models.CharField(max_length=200, help_text="Title of the property (e.g., Spacious 3-Bedroom House)")
    description = models.TextField(help_text="Detailed description of the property")
    price = models.DecimalField(max_digits=12, decimal_places=2, help_text="Price of the property in USD")
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES, help_text="Type of property")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='sale', help_text="Property status")
    bedrooms = models.IntegerField(null=True, blank=True, help_text="Number of bedrooms")
    bathrooms = models.IntegerField(null=True, blank=True, help_text="Number of bathrooms")
    square_feet = models.IntegerField(null=True, blank=True, help_text="Total area in square feet")
    location = models.CharField(max_length=255, help_text="Location of the property (e.g., City, State)")
    image = models.ImageField(upload_to='property_images/', null=True, blank=True, help_text="Main image of the property")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.title
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 800 or img.width > 800:
                output_size = (800, 800)
                img.thumbnail(output_size)
                img.save(self.image.path)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True, blank=True)
    image = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

    class Meta:
     db_table ='properties_profile'

class Agent(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    image = models.ImageField(upload_to='agent_images/', null=True, blank=True)

    def _str_(self):
        return self.name


class Question(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Question from {self.name} on {self.created_at}"



