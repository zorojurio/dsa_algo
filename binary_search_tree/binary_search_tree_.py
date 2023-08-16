from queue import Queue


class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None

    def __str__(self):
        return f'{self.data}'

    def __repr__(self):
        return f'{self.data}'


def insert(root_node, value):
    if root_node is None:
        root_node.data = value
    else:
        if value <= root_node.data:
            if root_node.left_node is None:
                new_node = BinarySearchTreeNode(value)
                root_node.left_node = new_node
            else:
                insert(root_node.left_node, value)
        else:
            if root_node.right_node is None:
                new_node = BinarySearchTreeNode(value)
                root_node.right_node = new_node
            else:
                insert(root_node.right_node, value)
        return f"Node {value} inserted"


def pre_order_traversal(root_node: BinarySearchTreeNode):
    if root_node is None:
        return None
    print(root_node.data, end='->')
    pre_order_traversal(root_node.left_node)
    pre_order_traversal(root_node.right_node)


def in_order_traversal(root_node: BinarySearchTreeNode):
    if root_node is None:
        return None
    else:
        in_order_traversal(root_node.left_node)
        print(root_node.data, end='->')
        in_order_traversal(root_node.right_node)


def post_order_traversal(root_node: BinarySearchTreeNode):
    if root_node is None:
        return None
    else:
        post_order_traversal(root_node.left_node)
        post_order_traversal(root_node.right_node)
        print(root_node.data, end='->')


def level_order_traversal(root_node: BinarySearchTreeNode):
    if root_node is None:
        return None
    else:
        custom_queue = Queue()
        custom_queue.put(root_node)
        while not custom_queue.empty():
            root = custom_queue.get()
            print(root.data, end="->")
            if root.left_node is not None:
                custom_queue.put(root.left_node)
            if root.right_node is not None:
                custom_queue.put(root.right_node)


if __name__ == '__main__':
    bst = BinarySearchTreeNode(70)
    print(insert(bst, 50))
    print(insert(bst, 90))
    print(insert(bst, 30))
    print(insert(bst, 60))
    print(insert(bst, 80))
    print(insert(bst, 100))
    print(insert(bst, 20))
    print(insert(bst, 40))
    pre_order_traversal(root_node=bst)
    print()
    in_order_traversal(root_node=bst)
    print()
    post_order_traversal(root_node=bst)
    print()
    level_order_traversal(root_node=bst)
    print()