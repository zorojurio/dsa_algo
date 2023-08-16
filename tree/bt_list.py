
class BinaryTree:
    def __init__(self, size):
        self.custom_list = [None] * size
        self.last_used_index = 0
        self.max_size = size

    def insert(self, value):
        if self.last_used_index + 1 == self.max_size:
            return "Full"
        else:
            self.custom_list[self.last_used_index+1] = value
            self.last_used_index += 1


new_binary_tree = BinaryTree(8)

new_binary_tree.insert('Drinks')
new_binary_tree.insert('Hot')
new_binary_tree.insert('Cold')
new_binary_tree.insert('Tea')
new_binary_tree.insert('Coffee')
print(new_binary_tree.custom_list)

