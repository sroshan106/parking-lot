import datetime;

# Defining a parking ticket class all
# data about particular ticket will be
# managed by this class
class Parking_Ticket:
    
    next_ticket_id = 1
    
    # Class Constructor used to initlize data
    # Assign a ticket to given vehicle number and person age
    def __init__(self, vehicle_number, parking_spot, age):
        
        # Generate a unique ticket
        self.__ticket_number = Parking_Ticket.next_ticket_id
        Parking_Ticket.next_ticket_id+=1
        
        # Store vehicle and person information as objects
        self.__vehicle_number = vehicle_number
        self.__person_age = age
        
        self.__date_time = datetime.datetime.now()
        self.__parking_spot = parking_spot
    
    def get_ticket_details(self):
        return [self.__vehicle_number,self.__person_age];
    
    def get_parking_spot(self):
        return self.__parking_spot