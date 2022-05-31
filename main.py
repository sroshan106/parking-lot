from parking_lot import ParkingLot

parking_instance = None
def list_to_comma_string(array):
    converted_array = [str(element) for element in array]
    return ','.join(converted_array)

    

def parse_line(input_line):

    global parking_instance
    
    if input_line[0] == 'Create_parking_lot':
        parking_capacity = int(input_line[1])
        
        # Execute parking lot generation command
        parking_instance = ParkingLot(parking_capacity)
        
        print("Created parking of {} slots".format(parking_capacity))
        
    
    elif input_line[0] == 'Park':
        vehicle_number = input_line[1]
        if input_line[2] == 'driver_age':
            driver_age = int(input_line[3])        
            parking_spot = parking_instance.allocate_parking(vehicle_number, driver_age)
            print('Car with vehicle registration number "{}" has been parked at slot number {}'.format(vehicle_number, parking_spot))
    
    elif input_line[0] == 'Slot_numbers_for_driver_of_age':
        person_age = int(input_line[1])
        # Execute find spot by person age
        age_occupied_spots = parking_instance.Slot_numbers_for_driver_of_age(person_age)
        age_occupied_spots = list_to_comma_string(age_occupied_spots)
        print(age_occupied_spots)
        
        

    elif input_line[0] == 'Slot_number_for_car_with_number':
        vehicle_number = input_line[1]
        # Execute find spot by vehicle_number
        spot = parking_instance.Slot_number_for_car_with_number(vehicle_number)
        print(spot)
    
    elif input_line[0] == 'Leave':
        spot = int(input_line[1])
        # Execute vacate command
        vehicle_number, person_age = parking_instance.deallocate_parking(spot)
        print('Slot number {} vacated, the car with vehicle registration number "{}" left the space, the driver of the car was of age {}'.format(spot, vehicle_number,person_age))
        
    
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
                    