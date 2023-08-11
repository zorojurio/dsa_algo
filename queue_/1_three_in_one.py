class MultiStack:
    def __init__(self, stack_size):
        self.number_of_stacks = 3
        self.custom_list = [0] * (self.number_of_stacks * stack_size)
        self.sizes = [0] * self.number_of_stacks
        self.stack_size = stack_size

    def is_full(self, stack_number):
        return self.sizes[stack_number] == self.stack_size

    def is_empty(self, stack_number):
        return self.sizes[stack_number] == 0

    def index_of_top(self, stack_number):
        offset = stack_number * self.stack_size
        return offset + self.sizes[stack_number] - 1

    def push(self, item, stack_number):
        if self.is_full(stack_number):
            return "Stack is Full"
        else:
            self.sizes[stack_number] += 1
            self.custom_list[self.index_of_top(stack_number)] = item

    def pop(self, stack_number):
        if self.is_empty(stack_number):
            return "Empty Stack"
        else:
            top_index = self.index_of_top(stack_number)
            value = self.custom_list[top_index]
            self.custom_list[top_index] = 0
            self.sizes[stack_number] -= 1
            return value

    def peek(self, stack_number):
        if self.is_empty(stack_number):
            return "Empty Stack"
        else:
            value = self.custom_list[self.index_of_top(stack_number)]
            return value


if __name__ == '__main__':
    custom_stack = MultiStack(6)
    print(custom_stack.is_full(0))
    print(custom_stack.is_full(1))
    print(custom_stack.is_full(2))
    print(custom_stack.is_empty(0))
    print(custom_stack.is_empty(1))
    print(custom_stack.is_empty(2))
    custom_stack.push(1, 0)
    custom_stack.push(2, 0)
    custom_stack.push(3, 2)
    print(custom_stack.peek(2))
    print(custom_stack.peek(0))
