from django.shortcuts import render
from .models import Event
from datetime import date

def event_list(request):
    events = Event.objects.filter(date__gte=date.today()).order_by('date')
    return render(request, "events/events_list.html", {"events": events})
