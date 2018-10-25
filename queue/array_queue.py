"""
Dynamic array-based queue implementation
"""


class ArrayQueue(object):
    def __init__(self, capacity):
        self._items = []
        self._capacity = capacity
        self._head = 0
        self._tail = 0

    def enqueue(self, item):
        if self._tail == self._capacity:
            if self._head == 0:
                return False
            else:
                for i in range(0, self._tail - self._head):
                    self._items[i] = self._items[i + self._head]
                self._tail = self._tail - self._head
                self._head = 0
        if self._tail == len(self._items):
            self._items.append(item)
        else:
            self._items[self._tail] = item
        self._tail += 1
        return True

    def dequeue(self):
        if self._head == self._tail:
            return
        else:
            item = self._items[self._head]
            self._head += 1
            return item

    def __str__(self):
        return ' '.join([str(item) for item in self._items[self._head : self._tail]])


if __name__ == "__main__":
    q = ArrayQueue(5)
    for i in range(5):
        q.enqueue(str(i))
        print(q._items)
    q.dequeue()
    q.dequeue()
    q.enqueue(str(5))
    q.enqueue(str(5))
    q.enqueue(str(5))
    print(q._items, q._head, q._tail)

