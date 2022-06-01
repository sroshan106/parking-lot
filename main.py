# Importing praking lot class
from parking_lot import Parking_Lot

# Global instance of parking lot to be shared by all functions
parking_instance = None

# Convert given integer list to commma
# separated string
# 
# returns String
def list_to_comma_string(array):
    converted_array = [str(element) for element in array]
    return ','.join(converted_array)

# Accepts and list input string and perform
# the required command on the parking lot instance
def parse_line(input_line):

    # global parking instance
    global parking_instance
    
    # Generate parking lot command
    if input_line[0] == 'Create_parking_lot':
        parking_capacity = int(input_line[1])
        
        # Execute parking lot generation command
        parking_instance = Parking_Lot(parking_capacity)
        print("Created parking of {} slots".format(parking_capacity))
    
    # Check if Parking lot is initialized before
    # performing any action
    if parking_instance==None:
        return "Parking not initialized"
    
    # Park a vehicle by vehicle number and driver age
    elif input_line[0] == 'Park':
        vehicle_number = input_line[1]
        if input_line[2] == 'driver_age':
            driver_age = int(input_line[3])        
            parking_spot = parking_instance.allocate_parking(vehicle_number, driver_age)
            print('Car with vehicle registration number "{}" has been parked at slot number {}'.format(vehicle_number, parking_spot))
    
    # Slot numbers of all slots where cars of drivers of a particular age are parked
    elif input_line[0] == 'Slot_numbers_for_driver_of_age':
        person_age = int(input_line[1])
        # Execute find spot by person age
        age_occupied_spots = parking_instance.Slot_numbers_for_driver_of_age(person_age)
        age_occupied_spots = list_to_comma_string(age_occupied_spots)
        print(age_occupied_spots)
        
    # Slot number in which a car with a given vehicle registration plate is parked.
    elif input_line[0] == 'Slot_number_for_car_with_number':
        vehicle_number = input_line[1]
        # Execute find spot by vehicle_number
        spot = parking_instance.Slot_number_for_car_with_number(vehicle_number)
        print(spot)
    
    # vacate function
    elif input_line[0] == 'Leave':
        spot = int(input_line[1])
        # Execute vacate command
        vehicle_number, person_age = parking_instance.deallocate_parking(spot)
        print('Slot number {} vacated, the car with vehicle registration number "{}" left the space, the driver of the car was of age {}'.format(spot, vehicle_number,person_age))
        
    # Vehicle Registration numbers for all cars which are parked by the driver of a certain age.
    elif input_line[0] == 'Vehicle_registration_number_for_driver_of_age':
        person_age = int(input_line[1])
        # Execute find vehicle_number by person age (comma separated)
        vehicle_numbers = parking_instance.Vehicle_registration_number_for_driver_of_age(person_age)
        print(','.join(vehicle_numbers))
    
    
    
# Loader and parser methode
if __name__ == "__main__":
    
    # Read input file line by line
    with open('input.txt','r') as file:
        for line in file:
            input_line =  line.strip().split(" ")
            parse_line(input_line)
                    