from django.contrib import admin
from .models import Location, Event, Review

admin.site.register(Location)
admin.site.register(Event)

# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('body', 'author', 'event', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('author', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


