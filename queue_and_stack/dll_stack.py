import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?

    def push(self, value):
        DoublyLinkedList.add_to_tail(self, value)

    def pop(self):
        DoublyLinkedList.remove_from_tail()

    def len(self):
        DoublyLinkedList.get_max(self)

