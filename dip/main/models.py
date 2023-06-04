from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.
class Location(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True, null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('location_detail', kwargs={'slug': self.slug})
    
class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    slug = models.SlugField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'location': self.location.slug, 'slug': self.slug})
    

class Review(models.Model):
    # title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    # slug = models.SlugField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.event.title

