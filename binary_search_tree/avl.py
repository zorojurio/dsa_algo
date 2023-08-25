from queue import Queue
from typing import Union


class AVlNode:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None
        self.height = 1

    def __repr__(self):
        return f"{self.data}"


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
    pre_order_traversal(root_node.right_child)


def in_order_traversal(root_node: AVlNode):
    if root_node is None:
        return None
    else:
        in_order_traversal(root_node.left_child)
        print(root_node.data, end='->')
        in_order_traversal(root_node.right_child)


def post_order_traversal(root_node: AVlNode):
    if root_node is None:
        return None
    else:
        post_order_traversal(root_node.left_child)
        post_order_traversal(root_node.right_child)
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


def get_height(root_node):
    if not root_node:
        return 0
    return root_node.height


def rotate_right(imbalanced_node: AVlNode) -> AVlNode:
    new_root: AVlNode = imbalanced_node.left_child
    imbalanced_node.left_child = imbalanced_node.left_child.right_child
    new_root.right_child = imbalanced_node
    imbalanced_node.height = 1 + max(get_height(imbalanced_node.right_child), get_height(imbalanced_node.left_child))
    new_root.height = 1 + max(get_height(new_root.right_child), get_height(new_root.left_child))
    return new_root


def rotate_left(imbalanced_node: AVlNode) -> AVlNode:
    new_root: AVlNode = imbalanced_node.right_child
    imbalanced_node.right_child = imbalanced_node.right_child.left_child
    new_root.left_child = imbalanced_node
    imbalanced_node.height = 1 + max(get_height(imbalanced_node.right_child), get_height(imbalanced_node.left_child))
    new_root.height = 1 + max(get_height(new_root.right_child), get_height(new_root.left_child))
    return new_root


def get_balance(root_node: AVlNode):
    if not root_node:
        return 0
    return get_height(root_node.left_child) - get_height(root_node.right_child)


def insert_node(root_node: AVlNode, node_value):
    if root_node is None:
        return AVlNode(node_value)
    elif node_value < root_node.data:
        node = insert_node(root_node.left_child, node_value)
        root_node.left_child = node
    else:
        node = insert_node(root_node.right_child, node_value)
        root_node.right_child = node
    root_node.height = 1 + max(get_height(root_node.left_child), get_height(root_node.right_child))
    balance = get_balance(root_node)
    if balance > 1 and node_value < root_node.left_child.data:
        rotate_node = rotate_right(root_node)
        return rotate_node
    if balance > 1 and node_value > root_node.left_child.data:
        rotate_left_node = rotate_left(root_node.left_child)
        root_node.left_child = rotate_left_node
        rotate_node = rotate_right(root_node)
        return rotate_node
    if balance < -1 and node_value > root_node.right_child.data:
        rotate_node = rotate_left(root_node)
        return rotate_node
    if balance < -1 and node_value < root_node.right_child.data:
        rotate_right_node = rotate_right(root_node.right_child)
        root_node.right_child = rotate_right_node
        rotate_node = rotate_left(root_node)
        return rotate_node
    return root_node


def get_minimum_value_node(root_node: AVlNode) -> Union[None, AVlNode]:
    """
    Find the minimum node value from the right subtree
    :param root_node: node of the right subtree
    :return: minimum node
    """
    if root_node is None or root_node.left_child is None:
        return root_node
    return get_minimum_value_node(root_node.left_child)


def delete_node(root_node: AVlNode, node_value):
    if not root_node:
        return root_node
    elif node_value < root_node.data:
        root_node.left_child = delete_node(root_node.left_child, node_value)
    elif node_value > root_node.data:
        root_node.right_child = delete_node(root_node.right_child, node_value)
    else:
        if root_node.left_child is None:
            temp = root_node.right_child
            return temp
        elif root_node.right_child is None:
            temp = root_node.left_child
            return temp
        temp = get_minimum_value_node(root_node.right_child)
        root_node.data = temp.data
        root_node.right_child = delete_node(root_node.right_child, temp.data)
    balance = get_balance(root_node)
    if balance > 1 and get_balance(root_node.left_child) >= 0:
        return rotate_right(root_node)
    if balance < -1 and get_balance(root_node.right_child) <= 0:
        return rotate_left(root_node)
    if balance > 1 and get_balance(root_node.left_child) < 0:
        root_node.left_child = rotate_left(root_node.left_child)
        return rotate_right(root_node)
    if balance < -1 and get_balance(root_node.right_child) < 0:
        root_node.right_child = rotate_right(root_node.right_child)
        return rotate_left(root_node)
    return root_node


def delete_avl(root_node: AVlNode):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None


if __name__ == '__main__':
    avl_tree = AVlNode(5)
    avl_tree = insert_node(avl_tree, 10)
    avl_tree = insert_node(avl_tree, 15)
    level_order_traversal(avl_tree)
    print()
    avl_tree = insert_node(avl_tree, 20)
    level_order_traversal(avl_tree)
    print()
    avl_tree = insert_node(avl_tree, 25)
    level_order_traversal(avl_tree)
    print('deleting 15')
    avl_tree = delete_node(avl_tree, 10)
    delete_avl(avl_tree)
    level_order_traversal(avl_tree)
