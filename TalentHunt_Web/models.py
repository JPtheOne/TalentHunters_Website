from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Hunter(models.Model):
    # Link to the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional fields
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    linkedin_profile = models.URLField(blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    # Add any other fields that you need for the Hunter profile

    def __str__(self):
        return self.user.username

# Create a Hunter profile for each new user
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Hunter.objects.create(user=instance)

# Save the Hunter profile when the user is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.hunter.save()
