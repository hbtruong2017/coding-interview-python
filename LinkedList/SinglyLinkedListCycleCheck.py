# Given a singly linked list, write a function which takes in the first node in a singly linked list 
# and returns a boolean indicating if the linked list contains a "cycle".

# A cycle is when a node's next point actually points back to a previous node in the list. 
# This is also sometimes known as a circularly linked list.

import unittest

class Node():
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None


def cycle_check(node):
    
    first_value = node.value

    while node.nextnode:

        next_node = node.nextnode

        if (next_node.value == first_value):
            return True

        node = next_node

    return False


# CREATE CYCLE LIST
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)


a.nextnode = b
b.nextnode = c
c.nextnode = d 
d.nextnode = a # Cycle Here!


# CREATE NON CYCLE LIST
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z


#############
class TestCycleCheck(unittest.TestCase):
    
    def test(self,sol):
        self.assertEqual(sol(a),True)
        self.assertEqual(sol(x),False)
        
        print("ALL TEST CASES PASSED")
        
# Run Tests

t = TestCycleCheck()
t.test(cycle_check)