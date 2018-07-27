import math

class priorityQueue:

    queue = [(0,0)]   #a list of pairs (element, priority) for representing the priority queue
                      #the intialization with (0,0) is for ease of implementation (indexing begins from 1)

    size = 0          #a variable for keeping track of the list elements number

    #a constructor for turning any collection into a priority queue
    def __init__(self, collection):
        for i in range(len(collection)):
            self.add(collection[i])

    #a method for satisfying the heap property after each addition of an entry (bottom - top)
    def heapifyTop(self, i):
        if (i > 1):
            if (self.queue[i][1] < self.queue[math.floor(i / 2)][1]):
                self.queue[i], self.queue[math.floor(i / 2)] = self.queue[math.floor(i / 2)], self.queue[i]
                self.heapifyTop(math.floor(i / 2))

    # a method for satisfying the heap property after each extraction of an entry (top - bottom)
    def heapifyBottom(self, i):
        #comparing the entry on the left with its parent
        if (i * 2 < len(self.queue) and self.queue[i][1] > self.queue[i * 2][1]):
            #comparing the entry on the right with its parent
            if ((i * 2) + 1 < len(self.queue) and self.queue[i][1] > self.queue[(i * 2) + 1][1]):
                #comparing the left and the right entries
                if (self.queue[(i * 2) + 1][1] < self.queue[i * 2][1]):
                    self.queue[i], self.queue[(i * 2) + 1] = self.queue[(i * 2) + 1], self.queue[i]
                    self.heapifyBottom((i * 2) + 1)
                else:
                    self.queue[i], self.queue[i * 2] = self.queue[i * 2], self.queue[i]
                    self.heapifyBottom(i * 2)
            else:
                self.queue[i], self.queue[i * 2] = self.queue[i * 2], self.queue[i]
                self.heapifyBottom(i * 2)
        #comparing the entry on the right with its parent
        elif ((i * 2) + 1 < len(self.queue) and self.queue[i][1] > self.queue[(i * 2) + 1][1]):
            self.queue[i], self.queue[(i * 2) + 1] = self.queue[(i * 2) + 1], self.queue[i]
            self.heapifyBottom((i * 2) + 1)

    #adds an entry (element, priority) to the list
    def add(self, entry):
        self.queue.append(entry)
        self.size = self.size + 1
        self.heapifyTop(len(self.queue)-1)

    #shows the minimum value in the priority queue
    def showMin(self):
        return self.queue[1]

    #returns the minimum value from the priority queue and deletes it completely
    def extractMin(self):
        if (self.size > 1):
            self.queue[1], self.queue[self.size] = self.queue[self.size], self.queue[1]
            min = self.queue.pop()
            self.size = self.size - 1
            self.heapifyBottom(1)   #always begins from the root
            return min
        elif (self.size == 1):
            self.size = self.size - 1
            return self.queue.pop()
        else:
            return -1   #if the priority queue is empty

    #prints the whole list of the priority queue
    def printQueue(self):
        print(self.queue[1 : self.size + 1])