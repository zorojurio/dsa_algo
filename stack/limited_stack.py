class Stack:
    def __init__(self, max_size):
        self.max_size = max_size
        self.list_ = []

    def __str__(self):
        return f'\n'.join([str(x) for x in self.list_[::-1]])

    def is_empty(self):
        return self.list_ == []

    def is_full(self):
        return len(self.list_) == self.max_size

    def push(self, value):
        if self.is_full():
            return "Stack is full"
        self.list_.append(value)
        return f"element {value} added correct"

    def pop(self):
        if self.is_empty():
            return "Empty Stack"
        else:
            return self.list_.pop()

    def peek(self):
        if self.is_empty():
            return "Empty Stack"
        else:
            return self.list_[len(self.list_) - 1]




stack = Stack(5)
print(stack.push(3))
print(stack.push(4))
print(stack.push(1))
print(stack.push(5))
print(stack.push(6))
print(stack.push(7))
print(stack)
print(stack.peek())

print()
print(stack.pop())

print()
print(stack)
