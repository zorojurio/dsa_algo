

class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


class Stack:
    def __init__(self):
        self.top = None
        self.min_node = None

    def __iter__(self):
        current_top = self.top
        while current_top:
            yield current_top
            current_top = current_top.next

    def __str__(self):
        return str([str(i) for i in self])

    def min(self):
        if not self.min_node:
            return None
        else:
            return self.min_node.value

    def push(self, item):
        if self.min_node and self.min_node.value < item:
            self.min_node = Node(value=self.min_node.value, next=self.min_node)
        else:
            self.min_node = Node(value=item, next=self.min_node)
        self.top = Node(value=item, next=self.top)

    def pop(self):
        if self.top is None:
            return None
        item = self.top.value
        self.min_node = self.min_node.next
        self.top = self.top.next
        return item


if __name__ == '__main__':
    stack = Stack()
    print(stack)
    stack.push(5)
    print(stack)
    print(stack.min())

    stack.push(6)
    print(stack)
    print(stack.min())

    stack.push(3)
    print(stack)
    print(stack.min())

    stack.pop()
    print(stack)
    print(stack.min())
