

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        temp_node = self.head
        while temp_node:
            yield temp_node
            temp_node = temp_node.next


class Stack:
    def __init__(self):
        self.linked_list = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.linked_list]
        return "\n".join(values)

    def is_empty(self):
        return self.linked_list.head is None

    def push(self, value):
        node = Node(value)
        node.next = self.linked_list.head
        self.linked_list.head = node

    def pop(self):
        if self.is_empty():
            return "Empty Stack"
        else:
            node = self.linked_list.head
            self.linked_list.head = self.linked_list.head.next
            return node.value

    def peek(self):
        if self.is_empty():
            return "Empty Stack"
        return self.linked_list.head.value

    def delete(self):
        self.linked_list.head = None


stack = Stack()
print(stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)


print("print peek", stack.peek())
print("***")
print(stack.pop())
print(stack)

print("***")
print(stack.pop())
print(stack)

print("***")
print(stack.pop())
print(stack)

print("***")
print(stack.pop())
print(stack)


print(stack.delete())
print(stack)
