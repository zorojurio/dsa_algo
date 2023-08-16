

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None

    def __str__(self):
        return f'{self.data}'

    def __repr__(self):
        return f'{self.data}'


if __name__ == '__main__':
    bst = BinarySearchTreeNode('Drinks')
