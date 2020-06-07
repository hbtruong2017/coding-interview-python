# Write a function that takes a head node and an integer value n 
# and then returns the nth to last node in the linked list. 
class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None
    
def nth_to_last_node(n, head):

    left_pointer = head
    right_pointer = head

    # Move right pointer n units from left pointer
    for i in range(n-1):

        if not right_pointer.nextnode:
            print("Error: n is larger than linked list")
            return

        right_pointer = right_pointer.nextnode

    # Set left_pointer
    while right_pointer.nextnode:
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode

    return left_pointer

import unittest

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

####

class TestNLast(unittest.TestCase):
    
    def test(self,sol):
        
        self.assertEqual(sol(2,a),d)
        print('ALL TEST CASES PASSED')
        
# Run tests
t = TestNLast()
t.test(nth_to_last_node)