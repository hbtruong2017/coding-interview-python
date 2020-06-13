"""
Given the Stack class below, implement a Queue class using two stacks! 
Note, this is a "classic" interview problem. 
Use a Python list data structure as your Stack.
"""

class QueueTwoStack():
    
    def __init__(self):

        self.inStack = []
        self.outStack = []

    def enqueue(self, item):

        self.inStack.append(item)

    def dequeue(self):

        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())
        return self.outStack.pop() 