class Queue(object):
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        return self.items.insert(0, item)    # The bracket version of this line indicates that we are going to insert the item at zeroth position.....
    
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
      
      
      
      
### Methods are :- Queue() = for creating a new empty queue.
###                isEmpty() = it checks whether a queue is empty or not.
###                enqueue() = for adding an element.
###                dequeue() = for removing an element.
###                size() = shows the no. of elements present in the queue.
