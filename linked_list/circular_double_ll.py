


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class CDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        temp = self.head
        while temp:
            yield temp
            temp = temp.next
            if temp == self.tail.next:
                break

    def create(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        node.prev = node
        node.next = node
        return True

    def insert(self, value, location):
        if self.head is None:
            return False
        node = Node(value)
        if location == 0:
            node.next = self.head
            node.prev = self.tail
            self.head.prev = node
            self.tail.next = node
            self.head = node
        elif location == -1:
            node.next = self.head
            node.prev = self.tail
            self.head.prev = node
            self.tail.next = node
            self.tail = node
        else:
            temp = self.head
            index = 0
            while index < location - 1:
                temp = temp.next
                index += 1
            node.next = temp.next
            node.prev = temp
            temp.next.prev = node
            temp.next = node
        return True

    def traverse(self):
        if self.head is None:
            return False
        else:
            temp = self.head
            while temp:
                print(temp.value)
                if temp == self.tail:
                    break
                temp = temp.next

    def reverse_traverse(self):
        if self.head is None:
            return False
        else:
            temp = self.tail
            while temp:
                print(temp.value)
                if temp == self.head:
                    break
                temp = temp.prev


if __name__ == '__main__':
    linked_list = CDLL()
    linked_list.create(5)
    print([node.value for node in linked_list])
    linked_list.insert(0, 0)
    print([node.value for node in linked_list])
    linked_list.insert(1,1)
    print([node.value for node in linked_list])
    linked_list.insert(2,2)
    print([node.value for node in linked_list])
    linked_list.insert(99, -1)
    print([node.value for node in linked_list])

    linked_list.reverse_traverse()

