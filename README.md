# Bus_Booking_Management_System

## Overview
This Bus Booking Management System is a Python-based project that facilitates easy and efficient management of bus bookings using MySQL as the database. The system provides a user-friendly interface for both administrators and customers, allowing them to perform various tasks related to bus reservations.

## Features
User Registration and Login: Users can create accounts and log in to the system.
Bus Search and Booking: Customers can search for available buses and make bookings.
Ticket Generation: The system generates tickets for confirmed bookings.
Admin Panel: Administrators have access to a dedicated panel for managing buses, bookings, and users.
Database Integration: MySQL is used to store and retrieve information related to buses, bookings, and users.

## Requirements
Python 3
MySQL Database


## Setup

## Clone the Repository:

git clone https://github.com/Rajesh-mm/Bus_Booking_Management_System.git
cd Bus_Booking_Management_System

## Install Dependencies:

pip install -r requirements.txt

## Database Setup:

Create a MySQL database and update the config.py file with your database details.
Import the provided SQL file (bus_booking.sql) into your MySQL database.

## Run the Application:

python main.py

## Usage
### User Login:
Users can log in using their registered credentials.

### Bus Search:
Search for available buses based on source, destination, and date.

### Booking:
Make a booking by selecting a suitable bus and providing passenger details.

### Ticket Generation:
Confirm the booking to generate a ticket with relevant details.

### Admin Panel:
Access the admin panel using the provided admin credentials.
Manage buses, view bookings, and monitor user activity.
