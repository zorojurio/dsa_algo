


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

    def search(self, value):
        if self.head is None:
            return False
        else:
            temp = self.head
            while temp:
                if value == temp.value:
                    return temp
                if self.tail == temp:
                    break
                temp = temp.next
            return False

    def delete(self, location):
        if self.head is None:
            return False
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head

            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head.prev = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                current_node = self.head
                index = 0
                while index < location - 1:
                    index += 1
                    current_node = current_node.next
                current_node.next = current_node.next.next
                current_node.next.prev = current_node
                return True

    def delete_entire_list(self):
        """
        Remove all the references to node so, they will be eligible for Garbage Collection
        :return:
        """
        if self.head is None:
            return False
        else:
            self.tail.next = None
            self.head.prev = None
            temp = self.head
            while temp:
                temp.prev = None
                temp = temp.next
            self.head = None
            self.tail = None
            print("Successfully Deleted the Linked List")


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

    # linked_list.reverse_traverse()
    # print("Searching")
    # print(linked_list.search(5).value)
    # print(linked_list.search(99).value)

    print("Deletion ")
    linked_list.delete(2)
    print([node.value for node in linked_list])
    linked_list.delete_entire_list()
    print([node.value for node in linked_list])

