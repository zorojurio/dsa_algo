
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

    def search(self, value):
        for i in range(len(self.custom_list)):
            if self.custom_list[i] == value:
                return True
        return False

    def pre_order_traversal(self, index=1):
        if index > self.last_used_index:
            return
        print(self.custom_list[index])
        self.pre_order_traversal(index*2)
        self.pre_order_traversal(index*2+1)


new_binary_tree = BinaryTree(8)

new_binary_tree.insert('Drinks')
new_binary_tree.insert('Hot')
new_binary_tree.insert('Cold')
new_binary_tree.insert('Tea')
new_binary_tree.insert('Coffee')
print(new_binary_tree.custom_list)
print(new_binary_tree.search('Tea'))
print("\npre order traversal")
new_binary_tree.pre_order_traversal()

