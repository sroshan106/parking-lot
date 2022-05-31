from  parkingSpot import Parking_Spots
from  parkingTicket import Parking_Ticket

# Defining the parking lot class.
# All the initialization, updation for parking lot will take place here.
class ParkingLot:

    # Constructor
    def __init__(self, total_capacity):
        self.__total_capacity = total_capacity
        self.__occupied_spots = 0
        self.__spot_instance = Parking_Spots(total_capacity)
        self.__active_tickets = {}
        # self.__spot_instance.print_spots();

    def print_details(self):
        print("total capacity " , self.__total_capacity);
        print("__occupied_spots " , self.__occupied_spots);
        print("__spot_instance " , self.__spot_instance);
        print("__active_tickets " , self.__active_tickets);
        
        
        print("parking spots " , self.__spot_instance.get_spots());
        
    # Check if parking is full
    def is_full(self):
        return self.__occupied_spots >= self.__total_capacity;

    # Increment current vehicle count
    def increment_occupied_count(self):
        self.__occupied_spots+=1

    # Decrement current vehicle count.
    def decrement_occupied_count(self):
        self.__occupied_spots-=1
        
    def allocate_parking(self, vehicle_number, age):
        if self.is_full():
            raise Exception('Parking Not Available')
        
        currentFreeSpot = self.__spot_instance.assign_parking_spot()
        if currentFreeSpot== None:
            raise Exception('Parking Not Available')

        ticket_object = Parking_Ticket(vehicle_number, currentFreeSpot, age)
        if ticket_object:
            self.__active_tickets[currentFreeSpot] = ticket_object
            self.increment_occupied_count();
        else :
            self.__spot_instance.vacate_parking_spot(currentFreeSpot)
        
        return currentFreeSpot
    
    def deallocate_parking(self,spot):
        if spot not in self.__active_tickets:
            raise Exception('Spot already vacant')
        occupied_at_spot_object = self.__active_tickets[spot]
        vehicle_number, person_age = occupied_at_spot_object.get_ticket_details()
        
        # vacate occupied ticket from active tickets 
        # and ticket heap
        self.__active_tickets.pop(spot)
        self.__spot_instance.vacate_parking_spot(spot)
        
        self.decrement_occupied_count();
        
        return [vehicle_number,person_age]
    
    def Slot_numbers_for_driver_of_age(self,age):
        
        active_spots = self.__active_tickets
        slot_numbers = []
        
        for current_spot in active_spots:
            vehicle_number,driver_age = active_spots[current_spot].get_ticket_details()
            if driver_age == age:
                slot_numbers.append(active_spots[current_spot].get_parking_spot())
        return slot_numbers 
    
    def Slot_number_for_car_with_number(self,number):
        
        active_spots = self.__active_tickets

        for current_spot in active_spots:
            vehicle_number,driver_age = active_spots[current_spot].get_ticket_details()
            if vehicle_number == number:
                return active_spots[current_spot].get_parking_spot()
        return -1

    def Vehicle_registration_number_for_driver_of_age(self,age):
        
        active_spots = self.__active_tickets
        vehicle_numbers = []
        
        for current_spot in active_spots:
            vehicle_number,driver_age = active_spots[current_spot].get_ticket_details()
            if driver_age == age:
                vehicle_numbers.append(vehicle_number)
        return vehicle_numbers
    