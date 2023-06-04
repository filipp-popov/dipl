from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from . models import Location, Event, Review, User
# Create your views here.


# def Event(request, slug, event, location):
#     template_name = 'profile.html'
#     infor = get_object_or_404(Event, slug=slug, event__slug=event, location__slug=location)
    
#     context = {'title': infor.name}
#     return render(request,template_name,context)

# def post_detail(request, slug):
#     post = get_object_or_404(Post, slug=slug)
#     return render(request, 'blog/post_detail.html', {'post': post})
class LocationListView(ListView):
    model = Location
    template_name = 'main/location_list.html'


class LocationDetailView(DetailView):
    model = Location
    template_name = 'main/location_detail.html'

class EventDetailView(DetailView):
    model = Event
    template_name = 'main/event_detail.html'