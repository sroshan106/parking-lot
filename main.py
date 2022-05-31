def parse_line(input_line):
    

    if input_line[0] == 'Create_parking_lot':
        parking_capacity = input_line[1]
        
        # Execute parking lot generation command
        continue
    
    if input_line[0] == 'Park':
        vehicle_number = input_line[1]
        if input_line[2] == 'driver_age':
            driver_age = input_line[3]
            
            # Execute add parking with details
            continue
    
    if input_line[0] == 'Slot_numbers_for_driver_of_age':
        person_age = input_line[1]
        # Execute find spot by person age
        continue

    if input_line[0] == 'Slot_number_for_car_with_number':
        vehicle_number = input_line[1]
        # Execute find spot by vehicle_number
        continue
    
    if input_line[0] == 'Leave':
        vehicle_number = input_line[1]
        # Execute vacate command
        continue
    
    if input_line[0] == 'Vehicle_registration_number_for_driver_of_age':
        person_age = input_line[1]
        # Execute find vehicle_number by person age (comma separated)
        continue
# Loader and parser methode
if __name__ == "__main__":
    
    # Read input file line by line
    with open('input.txt','r') as file:
        for line in file:
            
            input_line =  line.strip().split(" ")
            parse_line(input_line)
            
            
            
                    