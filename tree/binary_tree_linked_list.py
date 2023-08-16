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