import sys
import heapq
  

class Parking_Spots:
      
    # Constructor to initlize required
    # parameters and invoke required functions
    def __init__(self, total_spots):
        self.capacity = total_spots+1
        self.spots=[]
        for i in range(1, self.capacity):
            self.spots.append(i)
        self.generate_spots()
        
    # create heap to use for spot allocation
    # and generation
    def generate_spots(self):
        heapq.heapify(self.spots)
 
    # free the occupied parking spot
    # and add it to the heap memory
    def free_parking_spot(self, released_spot):
        heapq.heappush(self.spots, released_spot)
    
    # assign parking spot and return
    # the required spot
    def assign_parking_spot(self):
        return heapq.heappop(self.spots)
    
    # print the list of available spots
    # currently in the system
    def print_spots(self):
        print(self.spots)
        
