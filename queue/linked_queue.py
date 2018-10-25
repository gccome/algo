"""
Linked list-based queue implementation
"""


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedQueue(object):
    def __init__(self):
        self._head = None
        self._tail = None

    def enqueue(self, value):
        new_node = Node(value)
        if self._tail is None:
