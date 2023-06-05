from django.contrib import admin
from .models import Location, Event, Review

admin.site.register(Location)
admin.site.register(Event)

# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('event', 'author', 'created_on', 'active')
    list_filter = ('active', 'created_on')

    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


