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
    

ob = ParkingLot(10)

ob.print_details()
print (" ***************************** ")

ob.allocate_parking("asdasd", 42)

ob.print_details()
print (" ***************************** ")


ob.allocate_parking("Fasd asdasd asda", 51)

ob.print_details()
print (" ***************************** ")


ob.allocate_parking("asdasd", 32)

ob.print_details()
print (" ***************************** ")


ob.deallocate_parking(2)

ob.print_details()
print (" ***************************** ")

ob.allocate_parking("testing new version", 91)

ob.print_details()
print (" ***************************** ")
