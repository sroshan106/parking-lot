import datetime;
import parkingSpot;

# Defining a parking ticket class all
# data about particular ticket will be
# managed by this class
class parking_ticket:
    
    # Class Constructor used to initlize data
    next_ticket_id = 1
    def __init__(self):
        
        self.__vehicle_number = None
        self.__ticket_number = None
        self.__date_time = None
        self.__parking_spot = None
    
    # Assign a ticket to given vehicle
    def assign_ticket(vehicle_number, parking_spot):
        
        self.__vehicle_number = vehicle_number
        self.__ticket_number = next_ticket_id
        next_ticket_id+=1
        self.__parking_spot = parkingSpot.Parking_Spots(total_capacity)
        self.__date_time = datetime.datetime.now()
