# We define a class named priorityQueue with the properties heap (which is created using a list) and count (just an int)

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.count = 0

    # A method push() adds an item with its priority to the heap (as a new list) and therefore to the Priority Queue.
    
    def push(self, item, priority):
        self.heap.append([item, priority])
        self.count += 1

    # A method pop() finds the item with the minimum priority, deletes it from the heap and returns it to the user
    # To do this, we assume that the item with the minimum priority is the first in the heap, and iterate the heap
    # in order to find whether there is an item with less priority or not. If so, we update the variable min.
    # After finding the item with the minimum priority, we store it and delete it from the heap. We then return it.
    # Remember that the heap contains lists [item, priority], so the priority of every item is in the 2nd index of the list.

    def pop(self):
        min = self.heap[0]
        for i in self.heap:
            if i[1] < min[1]:
                min = i
        item = self.heap[self.heap.index(min)]
        self.heap.pop(self.heap.index(min))
        self.count -= 1
        return item[0]

    # Returns the size of Priority Queue
    def size(self):
        return self.count

    # A method isEmpty() returns True if the Priority Queue is Empty and False if it is not. This is found using
    # the length of the heap which depicts the Priority Queue.

    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False

    # A method update() takes an item with its priority and finds whether it exists in the Priority Queue or not.
    # If it exists and its new priority is less than the existing one, the priority is updated, else the existing
    # priority remains untouched. If the item doesn't exist in the Priority Queue, it is added in the heap.

    def update(self, item, priority):
        for i in self.heap:
            if i[0] == item:
                if i[1] > priority:
                    i[1] = priority
                return
        self.heap.append([item, priority])
        self.count += 1

# The function PQSort() sorts a given list of integers using the Priority Queue implented above. We just insert every number from the list
# to the Priority Queue with a priority same as the number. After that, we pop every item beginning from the one with the
# minimum priority (which means that the number is also less than the others) and appends it to a new list which is returned
# to the user.

def PQSort(list):
    pqueue = PriorityQueue()
    for number in list:
        pqueue.push(number, number)
    sorted_list = []
    while pqueue.isEmpty() == False:
        sorted_list.append(pqueue.pop())
    return sorted_list
