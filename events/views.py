from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import *
from .forms import VenueForm, MessageForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)

    context = {
        "venue": venue
    }
    return render(request, 'events/venue_detail.html', context)

def list_venues(request):
    venue_list = Venue.objects.all()
    context = {
        "venue_list": venue_list
    }
    return render(request, 'events/venue_list.html', context)

def add_venue(request):
    submitted = False
    if request.method == "POST":
        filled_form = VenueForm(request.POST)
        if filled_form.is_valid():
            filled_form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm()
        if 'submitted' in request.GET:
            submitted = True
    context = {"form": form, "submitted": submitted}
    return render(request, 'events/venue.html', context)

def contact(request):
    if request.method == "POST":
        filled_form = MessageForm(request.POST)
        firstname = request.POST["first_name"]
        lastname = request.POST["last_name"]
        email = request.POST["email"]
        message = request.POST["message"]
        if filled_form.is_valid():
            filled_form.save()
            context = {
                "firstname": firstname,
                "lastname": lastname,
                "email": email,
                "message": message,
            }
            send_mail(
                firstname, # subject
                message, # message
                email, # from email
                ["mirozwering@gmail.com", "mirozwering@me.com"], # to email
                fail_silently=False,
            )
            return render(request, 'events/contact.html', context)
    form = MessageForm()
    context = {"form": form,}
    return render(request, 'events/contact.html', context)



def all_events(request):
    event_list = Event.objects.all()
    context = {
        "event_list": event_list
    }
    return render(request, 'events/event_list.html', context)


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    print("TEST:", month)
    name = "John"
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)




    cal = HTMLCalendar().formatmonth(
        year,
        month_number,
    )

    now = datetime.now()
    current_year = now.year
    time = now.strftime('%I:%M %p')
    
    context = {
        "name": name,
        "year": year,
        "month": month,
        "month_number": month_number,
        "cal": cal,
        "current_year": current_year,
        "time": time,
    }

    return render(request, 'events/home.html', context)
