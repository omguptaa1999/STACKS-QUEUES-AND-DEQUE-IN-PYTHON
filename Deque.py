class Deque(object):
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def addFront(self, item):
        return self.items.append(item)
    
    def addRear(self, item):
        return self.items.insert(0, item)
    
    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
      
      
      
      
### Methods are :- Deque() - creating a new empty deque , isEmpty() - Empty or Not Empty , addFront() - adds in the Front , addRear() - adds in the Rear/Back , removeFront() - removes from the Front , removeRear() - remove from the Rear/Back , size() - no. of the elements present in the deque.
