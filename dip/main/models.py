from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Location(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.title
    
class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    slug = models.SlugField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

class Review(models.Model):
    # title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    # slug = models.SlugField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.event.title

