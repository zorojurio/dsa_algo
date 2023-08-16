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
