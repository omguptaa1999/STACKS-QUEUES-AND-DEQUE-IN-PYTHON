class Stack(object):
    
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self,item):
        return self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):       # Peek() shows which element is on the top position in stack... 
        return self.items[len(self.items)-1]
    
    def size(self):
        return len(self.items)
      
      

### Methods are :-    Stack() = for creating a new empty stack.
###                   isEmpty() = it checks whether a stack is empty or not.
###                   push() = adding new item.
###                   pop() = removes an item from the peek/top.
###                   peek() = shows the value at top/peek.
###                   size() = shows the no. of elements present in the stack.
