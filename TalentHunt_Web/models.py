from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.db import models
from django.contrib.auth.models import User

class Hunter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    linkedin_profile = models.URLField(blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    hunter = models.ForeignKey(Hunter, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    required_skills = models.CharField(max_length=200)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class SimpleModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Hunter2(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=50)  # Mejor usar django.contrib.auth.models.User para contraseñas
    full_name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    industry = models.CharField(max_length=200, blank=True, null=True)

class Project2(models.Model):
    hunter = models.ForeignKey(Hunter2, on_delete=models.CASCADE)  # Relacionar con Hunter2
    title = models.CharField(max_length=200)
    description = models.TextField()
    required_skills = models.CharField(max_length=300)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=100)
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in-progress', 'In Progress'),
        ('completed', 'Completed')
    ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)