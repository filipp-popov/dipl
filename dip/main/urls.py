from django.urls import path, re_path
from django.conf.urls.static import static
from django.conf import settings
from .views import LocationDetailView, LocationListView, EventDetailView
from . import views




urlpatterns = [
    path('', LocationListView.as_view(), name='location_list'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),
    path('<str:location>/<slug:slug>/', views.event_detail, name='event_detail'),
    # path('<str:location>/<slug:slug>/', EventDetailView.as_view(), name='event_detail'),
    # path('<slug:slug>/', views.event_detail, name='event_detail')
    path('<slug:slug>', LocationDetailView.as_view(), name='location_detail'),
  
    
    # path('add_venue/', views.add_venue, name='add-venue'),
    # re_path(r'^(?P<year>[0-9]{4})/(?P<month>0?[1-9]|1[0-2])/', views.index, name='index'),
    # path(r'^(?P<location>[\w-]+)/(?P<event>[\w-]+)/(?P<slug>[\w-]+)/$', Event, name='profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
