"""
Array-based circular queue implementation
"""


class CircularQueue(object):
    def __init__(self, capacity):
        self._capacity = capacity + 1
        self._items = []
        self._head = 0
        self._tail = 0

    def enqueue(self, item):
        if (self._tail + 1) % self._capacity == self._head:
            return False
        if self._tail == len(self._items):
            self._items.append(item)
        else:
            self._items[self._tail] = item
        self._tail = (self._tail + 1) % self._capacity
        return True

    def dequeue(self):
        if self._head == self._tail:
            return
        item = self._items[self._head]
        self._head = (self._head + 1) % self._capacity
        return item

    def __str__(self):
        if self._tail >= self._head:
            return ' '.join([str(item) for item in self._items[self._head : self._tail]])
        else:
            return ' '.join([str(item) for item in self._items[self._head:] + self._items[:self._tail]])


if __name__ == "__main__":
    q = CircularQueue(5)
    print(q._items)
    for i in range(5):
        q.enqueue(str(i))
        print(q)
    q.dequeue()
    q.dequeue()
    q.enqueue(str(5))
    q.enqueue(str(6))
    q.dequeue()
    q.enqueue(str(6))
    q.enqueue(str(7))

    print(q)
