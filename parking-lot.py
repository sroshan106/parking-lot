import parkingSpot
import pdb

# Defining the parking lot class.
# All the initialization, updation for parking lot will take place here.
class ParkingLot:

    # Constructor
    def __init__(self, total_capacity):
        self.__total_capacity = total_capacity
        self.__vehicle_count = 0
        self.__spot_instance = parkingSpot.Parking_Spots(total_capacity)
        # self.__spot_instance.print_spots();

    # Check if parking is full
    def is_full(self):
        return self.__vehicle_count < total_capacity;

    # Increment current vehicle count
    def increment_vehicle_count(self):
        self.__vehicle_count+=1

    # Decrement current vehicle count.
    def decrement_vehicle_count(self):
        self.__vehicle_count-=1
        
    def allocate_parking(self):
        if self.is_full():
            raise Exception('Parking Not Available')
        
        #Todo - generate ticket using vehicle and user detail
        self.increment_vehicle_count();
    
    def deallocate_parking(self,ticket):
        # Todo - Read ticket and mark occupied space as empty

        self.decrement_vehicle_count();
    
    
ob = ParkingLot(10)