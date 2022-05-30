import sys
  
class Parking_Spots:
  
    def __init__(self, total_spots):
        self.total_spots = total_spots
        self.size = 0
        self.Heap = [0]*(self.total_spots + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1
        self.generateHeap()

    def generateHeap(self):
        for i in range(1,self.total_spots+1):
            self.insert(i)
            
  
    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        return pos//2
  
    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):
        return 2 * pos
  
    # Function to return the position of
    # the right child for the node currently
    # at pos
    def rightChild(self, pos):
        return (2 * pos) + 1
  
    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):
        return pos*2 > self.size
  
    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]
  
    # Function to heapify the node at pos
    def minHeapify(self, pos):
  
        # If the node is a non-leaf node and greater
        # than any of its child
        if not self.isLeaf(pos):
            if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or 
               self.Heap[pos] > self.Heap[self.rightChild(pos)]):
  
                # Swap with the left child and heapify
                # the left child
                if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
  
                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))
  
    # Function to insert a node into the heap
    def insert(self, element):
        if self.size >= self.total_spots :
            return
        self.size+= 1
        self.Heap[self.size] = element
  
        current = self.size
  
        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
  

    # Function to build the min heap using
    # the minHeapify function
    def minHeap(self):
  
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)
  
    # Function to remove and return the minimum
    # element from the heap
    def remove(self):
  
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size-= 1
        self.minHeapify(self.FRONT)
        return popped
                            