# Django-based Airline Reservation System 🛫

The app stores information about airports, flights, passengers, and bookings. Users will be able to view flights, book a flight using a unique booking code generated with uuid, and check their reservations without authentication. 

## Project Structure

- **Models**:
  - `Airport` : 3-letter airport code and city name
  - `Flight` : origin, destination (both foreign keys to Airport), duration (in minutes), and capacity
  - `Passenger` :  passenger name and email address
  - `Booking` : passenger (foreign key to Passenger), flight (foreign key to Flight), booking_code

- **Pages**:
  - **Index Page**: Displays all flights, users can view airport and flight details
  - **Flight Page**: Shows flight details and booked passengers, users can book this flight
  - **Booking Page**: Has a form that takes user’s name and email address as an input
  - **Booking Confirmation**: Displays the unique booking code
  - **Manage Booking**: Has a form that takes booking code as input, if the code is correct shows the flight details otherwise sends them to an error page
  - **Airport Page**: Displays arriving and departing flights for particular airport

## Tech Stack

- **Backend**: Django, Python
- **Database**: SQLite (Populated DB with 10 airports & 20 flights beforehand using Django ORM in the shell)
- **Frontend**: HTML, CSS (Applied basic styling)

## Project Overview

### Homepage - index.html
![Homepage](https://github.com/user-attachments/assets/fe8f1d35-79b8-4fbf-bfc3-71876ee621fb)

### Airport Details - airport_detail.html
![Airport Details](https://github.com/user-attachments/assets/4d988806-3797-4c26-b1de-32a45377e344)

### Flight Details - flight_detail.html
![Flight Details](https://github.com/user-attachments/assets/a1160b7e-1577-4b8f-ac6e-329825a2eaff)

### Booking Form - booking.html
![Booking](https://github.com/user-attachments/assets/5fe40051-4d0e-4885-b106-2928525ef26a)

### Booking Confirmation - booking_confirmation.html
![Booking Confirmation](https://github.com/user-attachments/assets/5410b88e-ee57-4505-bb14-22b5829d7a6d)

### Manage Booking Form - manage_booking.html
![Booking Form](https://github.com/user-attachments/assets/71a8ed78-b0f5-4b11-a284-c35503c60c28)

### Error Note - error.html
![Error Note](https://github.com/user-attachments/assets/eb2cb8e7-d072-46c9-9f51-ed65a3c3eac0)

### Booking Details - booking_details.html
![Manage Booking](https://github.com/user-attachments/assets/2664183c-e7cd-489c-9a46-dccf582d7031)
