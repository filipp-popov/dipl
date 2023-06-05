from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView


from .forms import NewUserForm, ReviewForm

from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm


from . models import Location, Event, Review, User

class LocationListView(ListView):
    model = Location
    template_name = 'main/location_list.html'


class LocationDetailView(DetailView):
    model = Location
    template_name = 'main/location_detail.html'

class EventDetailView(DetailView):
    model = Event
    template_name = 'main/event_detail.html'

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("location_list")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="main/register.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("location_list")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("location_list")


def event_detail(request, location, slug):
    template_name = 'main/review_detail.html'
    rev = Review.objects.filter(event__slug=slug).filter(event__location__slug=location)
    ev = Event.objects.get(slug=slug)
    reviews = rev.filter(active=True)
    new_review = None
    # Review posted
    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            


            new_review = review_form.save(commit=False)
            new_review.event = ev


            new_review.author = request.user

            new_review.save()
    else:
        review_form = ReviewForm()

    return render(request, template_name, {'event': ev,
                                           'reviews': reviews,
                                           'new_review': new_review,
                                           'review_form': review_form})