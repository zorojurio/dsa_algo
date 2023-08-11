

class StackPlate:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []

    def __str__(self):
        return str(self.items)

    def push(self, item):
        if self.items and len(self.items[-1]) < self.capacity:
            self.items[-1].append(item)
        else:
            self.items.append([item])

    def pop(self):
        while len(self.items) and len(self.items[-1]) == 0:
            self.items.pop()
        if len(self.items) == 0:
            return None
        else:
            return self.items[-1].pop()

    def pop_at(self, stack_number):
        if len(self.items[stack_number]) > 0:
            return self.items[stack_number].pop()
        else:
            return None


if __name__ == '__main__':
    custom = StackPlate(2)
    custom.push(1)
    custom.push(2)
    custom.push(3)
    custom.push(4)
    print(custom)
    custom.pop()
    print(custom)
    custom.pop_at(0)
    print(custom)


# [[1, 2], [3, 4]]
# [[1, 2], [3]]
# [[1], [3]]
