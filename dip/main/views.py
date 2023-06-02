from django.shortcuts import render
from . models import Location, Event, Review, User
# Create your views here.


def homepage(request):

    title = "Gorod kvestov"
    # brand_name = Brand.objects.all().first()
    # all_quests = Quest.objects.all()

    return render(request, 'main/homepage.html', {'title':title, 'brand_name':brand_name, 'all_quests':all_quests})