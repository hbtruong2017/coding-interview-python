class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
    
    # def printList(self):
    #     temp = self.head
    #     while(temp):
    #         print(temp.data)
    #         temp = temp.next_node

if __name__ == '__init__':

    second = Node(2)
    third = Node(3)

    doubly_linked_list = DoublyLinkedList()
    doubly_linked_list.head = Node(1)

    doubly_linked_list.next_node = second
    second.prev_node = doubly_linked_list.head

    second.next_node = third
    third.prev_node = second

    # doubly_linked_list.printList()


    