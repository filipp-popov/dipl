from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from django.conf import settings
User = settings.AUTH_USER_MODEL

# Create your models here.

def loc_path(instance, filename):
    return '{0}/{1}' .format(instance.title, filename) 

class Location(models.Model):
    title = models.CharField(max_length=50)

    description = models.TextField(max_length=500, blank=True, null=True)
    slug = models.SlugField()
    img = models.ImageField(upload_to=loc_path, blank=True, null=True)


    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('location_detail', kwargs={'slug': self.slug})

def event_path(instance, filename):
    return '{0}/{1}' .format(instance.title, filename) 

class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    slug = models.SlugField()
    img = models.ImageField( upload_to=event_path , blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('event_detail', kwargs={'location': self.location.slug, 'slug': self.slug})
    

class Review(models.Model):
    # title = models.CharField(max_length=50)
    body = models.TextField(max_length=500)
    # slug = models.SlugField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    active = models.BooleanField(default=False)


    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.event, self.author)







