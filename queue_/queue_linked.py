class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}"


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next


class Queue:
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linked_list]
        return '\n'.join(values)

    def enqueue(self, value):
        node = Node(value)
        if self.linked_list.head is None:
            self.linked_list.head = node
            self.linked_list.tail = node
        else:
            self.linked_list.tail.next = node
            self.linked_list.tail = node

    def is_empty(self):
        return self.linked_list.head is None

    def dequeue(self):
        if self.is_empty():
            return "Empty Queue"
        else:
            temp_node = self.linked_list.head
            if self.linked_list.head == self.linked_list.tail:
                self.linked_list.head = None
                self.linked_list.tail = None
            else:
                self.linked_list.head = self.linked_list.head.next
            return temp_node


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print("***********")
    queue.dequeue()
    print(queue)

    print("***********")
    queue.dequeue()
    print(queue)

    print("***********")
    queue.dequeue()
    print(queue)

    print("***********")
    queue.dequeue()
    print(queue)

