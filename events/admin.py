from django.contrib import admin
from .models import *

class MyClubUserAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name", "last_name", "email", ]
    ordering = ["-id"]
 

class VenueAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "phone", "id"]
    ordering = ["name"]
    search_fields = ["name", "address"]

class EventAdmin(admin.ModelAdmin):
    fields = [("name", "venue"), "event_date", "description", "manager"]
    list_display = ["name", "event_date", "venue"]
    ordering = ["-event_date"]
    list_filter = ["event_date", "venue"]

admin.site.register(Venue, VenueAdmin)
admin.site.register(MyClubUser, MyClubUserAdmin)
admin.site.register(Event, EventAdmin)
