from django.shortcuts import render, redirect
from amadeus import Client, ResponseError
from datetime import datetime, timedelta
from django.contrib import messages
from flights.forms import Search
from flights.models import Flights, Stops, Times, Dates
import requests
from django import template
import airportsdata
register = template.Library()

amadeus = Client(client_id='TDq6QgMJLBHmhEPEOyHJDO3QbPjYZ3V7',client_secret='G46vXh0BX1GrpNYC')

def home(request):
    Flights.objects.filter(user=request.user).delete()
    form = Search()
    if(request.method == 'POST'):
        form = Search(request.POST)
        if(form.is_valid()):
            source = form.cleaned_data['source']
            source = source.upper()
            destination = form.cleaned_data['destination']
            adults = form.cleaned_data['adults']
            depart = form.cleaned_data['depart']
            destination = destination.upper()
            my_datetime = datetime(depart.year, depart.month, depart.day)
            if my_datetime < datetime.now():
                return redirect('/flights/')
            if source == destination:
                return redirect('/flights/')
            airports = airportsdata.load('IATA')
            if source not in airports or destination not in airports:
                return redirect('/flights/')
            if adults < 1:
                return redirect('/flights/')
            purpose = amadeus.shopping.flight_offers_search.get(
                originLocationCode=source,
                destinationLocationCode=destination,
                departureDate=depart,
                adults=adults,
                max=5
            )
            for i in range(0,5):
                cost = float(purpose.data[i]['price']['total']) * 1.1
                new_flight = Flights(user=request.user, cost=cost)
                new_flight.save()
                for j in range(len(purpose.data[i]['itineraries'][0]['segments'])):
                    stop = Stops(location=purpose.data[i]['itineraries'][0]['segments'][j]['departure']['iataCode'])
                    stop.save()
                    new_flight.stops.add(stop)
                    stop = Stops(location=purpose.data[i]['itineraries'][0]['segments'][j]['arrival']['iataCode'])
                    stop.save()
                    new_flight.stops.add(stop)
                    orig=purpose.data[i]['itineraries'][0]['segments'][j]['departure']['at']
                    sep=orig.split('T')
                    time = Times(time=sep[1])
                    time.save()
                    new_flight.times.add(time)
                    date = Dates(date=sep[0])
                    date.save()
                    new_flight.dates.add(date)
            return redirect('/flights/results')
    context = {'form':form}
    return render(request, "flights/search.html",context)
def results(request):
    context = {'flights': [],'list': []}
    date = []
    time = []
    stops = []
    flights = Flights.objects.filter(user=request.user)
    context['flights'] = flights
    for obj in flights:
        for d in obj.dates.all():
            date.append(d.date)
        for t in obj.times.all():
            time.append(t.time)
        for s in obj.stops.all():
            stops.append(s.location)
    list = zip(date, time, stops)
    context['list'] = list
    return render(request, 'flights/results.html',context)
