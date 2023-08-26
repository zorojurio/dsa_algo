from queue import Queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return f"{self.data}"


def preorder_traversal(root_node):
    if root_node is None:
        return None
    print(root_node.data)
    preorder_traversal(root_node.left_child)
    preorder_traversal(root_node.right_child)


def inorder_traversal(root_node: TreeNode):
    if root_node is None:
        return None
    inorder_traversal(root_node.left_child)
    print(root_node.data)
    inorder_traversal(root_node.right_child)


def post_order_traversal(root_node: TreeNode):
    if root_node is None:
        return None
    post_order_traversal(root_node=root_node.left_child)
    post_order_traversal(root_node=root_node.right_child)
    print(root_node.data)


def level_order_traversal(root_node: TreeNode):
    if root_node is None:
        return None
    else:
        custom_queue = Queue()
        custom_queue.put(root_node)
        while not custom_queue.empty():
            root = custom_queue.get()
            print(root.data)
            if root.left_child is not None:
                custom_queue.put(root.left_child)
            if root.right_child is not None:
                custom_queue.put(root.right_child)


def search_binary_tree(root_node: TreeNode, node_value):
    if root_node is None:
        return "The Binary Tree does not exist"
    else:
        custom_queue = Queue()
        custom_queue.put(root_node)
        while not custom_queue.empty():
            root = custom_queue.get()
            if root.data == node_value:
                return root
            if root.left_child is not None:
                custom_queue.put(root.left_child)
            if root.right_child is not None:
                custom_queue.put(root.right_child)
        return f'{node_value} does not exists in the tree'


def insert_node(root_node: TreeNode, node_value):
    node = TreeNode(node_value)
    if root_node is None:
        root_node = node
        return root_node
    else:
        custom_queue = Queue()
        custom_queue.put(root_node)
        while not custom_queue.empty():
            root = custom_queue.get()
            if root.data == node_value:
                return root
            if root.left_child is not None:
                custom_queue.put(root.left_child)
            else:
                root.left_child = node
                return node
            if root.right_child is not None:
                custom_queue.put(root.right_child)
            else:
                root.right_child = node
                return node


def get_deepest_node(root_node: TreeNode):
    root = None
    if root_node is None:
        return None
    else:
        custom_queue = Queue()
        custom_queue.put(root_node)
        while not custom_queue.empty():
            root = custom_queue.get()
            if root.left_child is not None:
                custom_queue.put(root.left_child)
            if root.right_child is not None:
                custom_queue.put(root.right_child)

        deepest_node_ = root
        return deepest_node_


def delete_deepest_node(root_node: TreeNode, deepest_node: TreeNode):
    if root_node is None:
        return None
    else:
        custom_queue = Queue()
        custom_queue.put(root_node)
        while not custom_queue.empty():
            root = custom_queue.get()
            if root is deepest_node:
                del root
                return
            if root.right_child:
                if root.right_child is deepest_node:
                    root.right_child = None
                    return
                else:
                    custom_queue.put(root.right_child)

            if root.left_child:
                if root.left_child is deepest_node:
                    root.left_child = None
                    return
                else:
                    custom_queue.put(root.left_child)


def delete_node_bt(root_node: TreeNode, node_value):
    if root_node is None:
        return None
    else:
        deepest_node = get_deepest_node(root_node)
        custom_queue = Queue()
        custom_queue.put(root_node)
        while not custom_queue.empty():
            root = custom_queue.get()
            if root.data == node_value:
                root.data = deepest_node.data
                delete_deepest_node(tree, deepest_node)
                return "Node Deleted"
            if root.left_child is not None:
                custom_queue.put(root.left_child)
            if root.right_child is not None:
                custom_queue.put(root.right_child)
        return "Failed to delete the node"


def delete_binary_tree(root_node: TreeNode):
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
    return "Deleted Successfully"


if __name__ == '__main__':
    tree = TreeNode('Drinks')
    left_child = TreeNode('Hot')
    right_child = TreeNode('Cold')
    tree.left_child = left_child
    tree.right_child = right_child
    tea = TreeNode('Tea')
    coffee = TreeNode('Coffee')
    left_child.left_child = tea
    left_child.right_child = coffee

    preorder_traversal(tree)
    print("**********************\n")
    inorder_traversal(root_node=tree)
    print("**********************\n")
    post_order_traversal(root_node=tree)
    print("**********************\n")
    level_order_traversal(root_node=tree)
    print("**********************\n")
    print(search_binary_tree(tree, 'Tea'))
    print(search_binary_tree(tree, 'Coffee'))
    print(search_binary_tree(tree, 'Lemon'))
    print("**********************\n")
    insert_node(root_node=tree, node_value='Fanta')
    level_order_traversal(tree)
    print("**********************\n")
    insert_node(root_node=tree, node_value='Cola')
    level_order_traversal(tree)

    print("**********************\n")
    deepest_nod = get_deepest_node(tree)
    print("Deepest Node", deepest_nod.data)
    delete_deepest_node(tree, deepest_nod)
    insert_node(tree, node_value=deepest_nod.data)
    print("********************** after deleting deepest Node \n")
    level_order_traversal(tree)
    print("**********************\n")
    print(f"Deleting a node, deepest Node is {get_deepest_node(tree)} will be replaced with Tea")
    print(delete_node_bt(tree, 'Tea'))
    level_order_traversal(tree)
    delete_binary_tree(tree)
