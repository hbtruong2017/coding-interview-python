# Write a function to reverse a Linked List in place. 
# The function will take in the head of the list as input and return the new head of the list.

class Node():

    def __init__(self, value):

        self.value = value
        self.nextnode = None
    
def reverse(head):
    current = head
    prev, nxt = None, None

    while current:
        nxt = current.nextnode
        current.nextnode = prev

        prev = current
        current = nxt

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d

print a.nextnode.value
print b.nextnode.value
print c.nextnode.value

reverse(a)

print d.nextnode.value
print c.nextnode.value
print b.nextnode.value


