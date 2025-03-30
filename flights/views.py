from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Flight, Airport, Passenger, Booking
from django.db import transaction
import uuid

def index(request):
    flights = Flight.objects.all()
    return render(request, 'flights/index.html', {'flights': flights})

def flight_detail(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    booked_passengers = flight.booking_set.all()
    remaining_seats = flight.remaining_seats()
    
    return render(request, 'flights/flight_detail.html', {
        'flight': flight,
        'booked_passengers': booked_passengers,
        'remaining_seats': remaining_seats
    })

def book_flight(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        # Validate input
        if not name or not email:
            messages.error(request, 'Please provide both name and email.')
            return render(request, 'flights/booking.html', {'flight': flight})
        
        try:
            with transaction.atomic():
                # Create or get passenger
                passenger, created = Passenger.objects.get_or_create(
                    email=email,
                    defaults={'name': name}
                )
                
                # Check flight capacity
                if flight.remaining_seats() <= 0:
                    messages.error(request, 'Sorry, this flight is fully booked.')
                    return render(request, 'flights/booking.html', {'flight': flight})
                
                # Create booking
                booking = Booking.objects.create(
                    passenger=passenger,
                    flight=flight
                )
                
                return render(request, 'flights/booking_confirmation.html', {
                    'booking_code': booking.booking_code,
                    'flight': flight
                })
        
        except Exception as e:
            messages.error(request, f'An error occurred: {str(e)}')
    
    return render(request, 'flights/booking.html', {'flight': flight})

def manage_booking(request):
    if request.method == 'POST':
        booking_code = request.POST.get('booking_code')
        
        try:
            # Try to find booking with the given code
            booking = Booking.objects.get(booking_code=uuid.UUID(booking_code))
            return render(request, 'flights/booking_details.html', {'booking': booking})
        
        except (Booking.DoesNotExist, ValueError):
            # If booking not found or invalid code
            return render(request, 'flights/error.html')
    
    return render(request, 'flights/manage_booking.html')

def airport_detail(request, airport_code):
    airport = get_object_or_404(Airport, code=airport_code)
    departing_flights = airport.departing_flights.all()
    arriving_flights = airport.arriving_flights.all()
    
    return render(request, 'flights/airport_detail.html', {
        'airport': airport,
        'departing_flights': departing_flights,
        'arriving_flights': arriving_flights
    })