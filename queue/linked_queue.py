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
            self._head = new_node
            self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
            
    def dequeue(self):
        if self._head is None:
            return False
        value = self._head.data
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        return value

    def __str__(self):
        values = []
        current = self._head
        while current:
            values.append(current.data)
            current = current.next
        return ' '.join([value for value in values])


if __name__ == "__main__":
    q = LinkedQueue()
    for i in range(10):
        q.enqueue(str(i))
    print(q)

    for _ in range(3):
        q.dequeue()
    print(q)

    q.enqueue("7")
    q.enqueue("8")
    print(q)

