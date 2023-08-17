from queue import Queue


class AVlNode:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None
        self.height = 1


def level_order_traversal(root_node: AVlNode):
    if root_node is None:
        return None
    else:
        custom_queue = Queue()
        custom_queue.put(root_node)
        while not custom_queue.empty():
            root = custom_queue.get()
            print(root.data, end="->")
            if root.left_child is not None:
                custom_queue.put(root.left_child)
            if root.right_child is not None:
                custom_queue.put(root.right_child)


def pre_order_traversal(root_node: AVlNode):
    if root_node is None:
        return None
    print(root_node.data, end='->')
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.left_child)


def in_order_traversal(root_node: AVlNode):
    if root_node is None:
        return None
    else:
        in_order_traversal(root_node.left_child)
        print(root_node.data, end='->')
        in_order_traversal(root_node.left_child)


def post_order_traversal(root_node: AVlNode):
    if root_node is None:
        return None
    else:
        post_order_traversal(root_node.left_child)
        post_order_traversal(root_node.left_child)
        print(root_node.data, end='->')


def search(root_node: AVlNode, value):
    if root_node is None:
        return None
    if root_node.data == value:
        print(f'Value {value} found')
    elif value <= root_node.data:
        if root_node.left_child and root_node.left_child.data == value:
            print(f'Value {value} found')
        else:
            search(root_node.left_child, value)
    else:
        if root_node.right_child and root_node.right_child.data == value:
            print(f'Value {value} found')
        else:
            search(root_node.right_child, value)


if __name__ == '__main__':
    avl_tree = AVlNode(10)
