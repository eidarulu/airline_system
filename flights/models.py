import uuid
from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=3, unique=True)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code} - {self.city}"

class Flight(models.Model):
    origin = models.ForeignKey(
        Airport,
        on_delete=models.CASCADE, 
        related_name='departing_flights'
    )
    destination = models.ForeignKey(
        Airport, 
        on_delete=models.CASCADE, 
        related_name='arriving_flights'
    )
    duration = models.IntegerField(help_text="Flight duration in minutes")
    capacity = models.IntegerField(default=180)

    def __str__(self):
        return f"{self.origin.code} → {self.destination.code}"

    def remaining_seats(self):
        return self.capacity - self.booking_set.count()

class Passenger(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

class Booking(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    booking_code = models.UUIDField(
        default=uuid.uuid4, 
        editable=False, 
        unique=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.passenger.name} - {self.flight} - {self.booking_code}"