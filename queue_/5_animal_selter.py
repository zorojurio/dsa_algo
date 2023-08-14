

class AnimalStack:
    def __init__(self):
        self.cat_stack = []
        self.dog_stack = []

    def enqueue(self, item, type_):
        if type_.lower() == 'cat':
            self.cat_stack.append(item)
        elif type_.lower() == 'dog':
            self.dog_stack.append(item)

    def dequeue_cat(self):
        if len(self.cat_stack) < 0:
            return None
        else:
            return self.cat_stack.pop()

    def dequeue_dog(self):
        if len(self.dog_stack) < 0:
            return None
        else:
            return self.dog_stack.pop()

    def dequeue_any(self):
        if len(self.cat_stack) < 0:
            return self.cat_stack.pop()
        else:
            return self.dog_stack.pop()


if __name__ == '__main__':
    animal_queue = AnimalStack()
    animal_queue.enqueue('Cat1', 'cat')
    animal_queue.enqueue('Cat2', 'cat')
    animal_queue.enqueue('Cat3', 'cat')
    animal_queue.enqueue('Cat4', 'cat')
    animal_queue.enqueue('Dog1', 'dog')
    animal_queue.enqueue('Dog2', 'dog')
    animal_queue.enqueue('Dog3', 'dog')
    print(animal_queue.dequeue_any())
    print(animal_queue.dequeue_dog())
    print(animal_queue.dequeue_cat())
