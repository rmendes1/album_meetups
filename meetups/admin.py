from django.contrib import admin
from .models import Meetup, Location, Participant

# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title', 'location' )
    prepopulated_fields = {'slug': ('title',)} #generates a slug automatically



admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Location)
admin.site.register(Participant)