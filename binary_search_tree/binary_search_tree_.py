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


def search(root_node: BinarySearchTreeNode, value):
    if root_node is None:
        return None
    if root_node.data == value:
        print(f'Value {value} found')
    elif value <= root_node.data:
        if root_node.left_node and root_node.left_node.data == value:
            print(f'Value {value} found')
        else:
            search(root_node.left_node, value)
    else:
        if root_node.right_node and root_node.right_node.data == value:
            print(f'Value {value} found')
        else:
            search(root_node.right_node, value)


def get_minimum_value_node(root_node: BinarySearchTreeNode):
    current = root_node
    while current.left_node is not None:
        current = current.left_node
    return current


def delete_node(root_node: BinarySearchTreeNode, node_value):
    if root_node is None:
        return root_node
    if node_value < root_node.data:
        left_deleted_node = delete_node(root_node.left_node, node_value)
        root_node.left_node = left_deleted_node
    elif node_value > root_node.data:
        right_deleted_node = delete_node(root_node.right_node, node_value)
        root_node.right_node = right_deleted_node
    else:
        """
        if the value of left node is None, take the right because left child is already none
        if there is a value for left child, and if right node is none take the left node 
        """
        if root_node.left_node is None:
            temp = root_node.right_node
            return temp
        if root_node.right_node is None:
            temp = root_node.left_node
            root_node = None
            return temp
        temp = get_minimum_value_node(root_node.right_node)
        root_node.data = temp.data
        special = delete_node(root_node.right_node, temp.data)
        root_node.right_node = special
    return root_node


def delete_bst(root_node: BinarySearchTreeNode):
    root_node.data = None
    root_node.left_node = None
    root_node.right_node = None
    return "the BST has been successfully deleted"


if __name__ == '__main__':
    bst = BinarySearchTreeNode(70)
    print(insert(bst, 50))
    print(insert(bst, 90))
    print(insert(bst, 30))
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
    print('deleting ')
    delete_node(bst, 70)
    level_order_traversal(root_node=bst)
    print()
    delete_bst(bst)
