# Instructions : Air management system
# Your goal is to build an airplanes traffic management system.


# Details
# Your program should rely on four classes: Airline, Airplane, Flight and Airport.
# Consider every plane can fly only once per day.

# The Airline class
# Attributes:
# id (str) A two letters code
# name (str)
# planes : A list of Airplanes belonging to this airline (see below the Airplane class)
# This class has no methods

import datetime as dt

class Airline:
    def __init__(self, id_al, name, planes = None):
        if planes is None:
            planes = []

        self.id_al = id_al
        self.name = name
        self.planes = planes


# The Airplane class
# Attributes:
# id (int)
# current_location : The Airport where the airplane is currently located (see below the Airport class)
# company : The airline this airplane belongs to (see above the Airline class)
# next_flights : The list of Flights. Every future flights of the airplane, 
# this list should always be sorted by datetime. (see below the Flight class)

class Airplane:
    def __init__(self, id_ap, current_location, company, next_flight = None):
        if next_flight is None:
            next_flight = []

        self.id_ap = id_ap
        self.current_location = current_location
        self.company = company
        self.next_flight = next_flight
        

# Methods:

# fly(self, destination): Make the airplane take off and land if a flight is scheduled 
# for this destination (see below the Flight class)
# location_on_date(self, date): Returns where the plane will be on this date
# available_on_date(self, date, location) : Returns True if the plane can fly from this location 
# on this date (it can fly if it is in this location on this date and if it doesn’t already have a flight planned).

    def fly(self,destination):
        for flight in self.next_flight:
            if flight.destination == destination:
                flight.take_off()
                flight.land()
                self.next_flight.remove(flight)
                return f'Flight {flight.id_f} completed'
        
        return 'No flight scheduled for this destination.'


    def location_on_date(self,date):
        for flight in self.next_flight:
            if flight.date == date:
                return flight.destination
        else:
            return self.current_location

    def available_on_date(self, date, location):
        plane_location = self.location_on_date(date)
        if plane_location != location:
            return False
        for flight in self.next_flight:
            if flight.date  == date:
                return False
            
        return True

# The Flight class
# Attributes:
# date : datetime.Date
# destination : The destination airport. (see below the Airport class)
# origin : The departure airport. (see below the Airport class)
# plane : The plane used during this flight. (see above the Airplane class)
# id (str) : The ID is an encoded string composed of the destination, the airlines code and the date.

class Flight:
    def __init__(self, date, destination, origin, plane, id_f):
        self.date = date
        self.destination = destination
        self.origin = origin
        self.plane = plane
        self.id_f = id_f

# Methods:
# Those methods are here only to update the rest of the system:
# take_off(self)
# land(self) : change the location of the plane when it reaches its destination

    def take_off(self):
        if self.plane in self.origin.planes:
            self.origin.planes.remove(self.plane)


    def land(self):
        if self.plane not in self.destination.planes:
            self.destination.planes.append(self.plane)
            self.plane.current_location = self.destination



# The Airport class
# Attributes:
# city : (str) The code of the city where the airport is located
# planes : The list of every plane that is currently in this airport. (see above the Airplane class)
# scheduled_departures : The list of flight - Every future flight from this airport, sorted by date. (see above the Flight class)
# scheduled_arrivals : The list of flight - Every future flight that will arrive to this airport, sorted by date. (see above the Flight class)

class Airport:
    def __init__(self, city, planes, scheduled_departures, scheduled_arrivals):
        self.city = city
        self.planes = planes
        self.scheduled_departures = scheduled_departures
        self. scheduled_arrivals = scheduled_arrivals

# Methods:
# schedule_flight(self, destination, datetime) :
# finds an available airplane from an airline, that serves the departure and the destination
# schedule the airplane for the flight
# info(self, start_date, end_date) : Displays every scheduled flight from start_date to end_date.

    def schedule_flight (self, destination, date):
        for airline in all_airlines:
            for plane in airline.planes: 
                if plane.available_on_date(date, self):
                    flight_id = f'{destination.city}{plane.company.id_al}{date.strftime("%Y%m%d")}'
                    flight = Flight(date, destination, self, plane, flight_id)

                    plane.next_flight.append(flight)
                    self.scheduled_departures.append(flight)
                    destination.scheduled_arrivals.append(flight)

                    return f'Flight {flight_id} scheduled.'
                
        return 'No available plane for this flight.'


    def info(self, start_date, end_date):
        flights_in_range = [f for f in self.scheduled_departures 
                            if start_date <= f.date <= end_date]
        if not flights_in_range:
            print(f"No flights from {self.city} between {start_date} and {end_date}")
        else:
            print(f"Flights from {self.city} between {start_date} and {end_date}:")
            for f in sorted(flights_in_range, key=lambda x: x.date):
                print(f"Flight {f.id_f}: {f.origin.city} -> {f.destination.city} on {f.date}")

all_airlines = []