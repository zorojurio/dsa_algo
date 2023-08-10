

class Queue:
    def __init__(self, max_size):
        self.items = max_size * [None]
        self.max_size = max_size
        self.start = -1
        self.top = -1

    def __str__(self):
        return str(self.items)

    def is_full(self):
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.max_size:
            return True
        else:
            return False

    def is_empty(self):
        return self.top == -1

    def enqueue(self, value):
        if self.is_full():
            return "Queue is full"
        if self.top + 1 == self.max_size:
            self.top = 0
        else:
            self.top += 1
            if self.start == -1:
                self.start = 0
        self.items[self.top] = value
        return "Element is inserted at the end of the Queue"

    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        else:
            # get items and value from the queue
            start_value = self.items[self.start]
            start = self.start
            # traverse the queue
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.max_size:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return start_value

    def peek(self):
        if self.is_empty():
            return "Empty Queue"
        return self.items[self.top]

    def delete(self):
        self.items = [None] * self.max_size
        self.start = -1
        self.top = -1


if __name__ == '__main__':
    queue = Queue(3)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue)
    print(queue.is_full())
    print(queue.is_empty())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print("is Q empty", queue.is_empty())
