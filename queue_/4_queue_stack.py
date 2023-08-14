class Stack:
    def __init__(self):
        self.list = []

    def __len__(self):
        return len(self.list)

    def push(self, item):
        self.list.append(item)

    def pop(self):
        if len(self.list) == 0:
            return None
        else:
            return self.list.pop()


class QueueStack:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        """
        push all to out stack by popping all from in stack and remove the top element
        and push all to instack by popping all from out stock
        :return:
        """
        while len(self.in_stack):
            self.out_stack.push(self.in_stack.pop())
        top_out = self.out_stack.pop()

        while len(self.out_stack):
            self.in_stack.push(self.out_stack.pop())
        return top_out


