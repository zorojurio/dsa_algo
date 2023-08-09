class Stack:
    def __init__(self):
        self.list_ = []

    def __str__(self):
        return f'\n'.join([str(x) for x in self.list_[::-1]])

    def is_empty(self):
        return self.list_ == []

    def push(self, value):
        self.list_.append(value)

    def pop(self):
        if self.is_empty():
            return "There is no element"
        return self.list_.pop()

    def peek(self):
        if self.is_empty():
            return "There is no element"
        return self.list_[len(self.list_) - 1]


stack = Stack()
print(stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.is_empty())
print("*********")

stack.pop()
stack.push(4)
stack.push(35)
print(stack)

print("**********")
print(stack.peek())

