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
   * When using an array there you would not have access to the pointers to the next and previous node
"""

from singly_linked_list import LinkedList


class OldStack:
    def __init__(self):
        self.size: int = 0
        self.storage: list = []

    def __len__(self) -> int:
        return self.size

    def push(self, value) -> bool:
        prev_size = self.size
        self.storage.append(value)
        self.size += 1
        if self.size > prev_size:
            return True
        return False

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop(self.size)
        return None


class Stack:
    def __init__(self):
        self.size: int = 0
        self.storage: LinkedList = LinkedList()

    def __len__(self) -> int:
        return self.size

    def push(self, value) -> bool:
        prev_size = self.size
        self.storage.add_to_tail(value)
        self.size += 1
        if self.size > prev_size:
            return True
        return False

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_tail()
        return None
