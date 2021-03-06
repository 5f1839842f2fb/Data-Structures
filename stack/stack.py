"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
from singly_linked_list.singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        return len(self.storage)

    def __str__(self):
        return str(self.storage)

    def push(self, value):
        self.storage.add_to_tail(value)

    def pop(self):
        if len(self.storage) > 0:
            return self.storage.remove_tail()


stacky = Stack()
print(stacky)
print(len(stacky))
stacky.push(1)
print(stacky)
print(len(stacky))
stacky.push(2)
stacky.push(3)
print(stacky)
print(len(stacky))