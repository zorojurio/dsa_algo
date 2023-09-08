class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def get_max_height(root: Node) -> int:
    if root is None:
        return 0
    return 1 + max(get_max_height(root.left), get_max_height(root.right))


def balanced(root: Node) -> bool:
    if root is None:
        return True
    if not balanced(root.left):
        return False
    if not balanced(root.right):
        return False

    left_height = get_max_height(root.left)
    right_height = get_max_height(root.right)
    if abs(left_height - right_height) > 1:
        return False
    return True


if __name__ == '__main__':
    tree = Node(3)
    tree.left = Node(9)
    tree.right = Node(20)
    tree.right.left = Node(15)
    tree.right.right = Node(7)
    print(get_max_height(tree))
    print('Balanced ', balanced(root=tree))

    node = Node(1)
    node.left = Node(2)
    node.right = Node(2)
    node.left.left = Node(3)
    node.left.right = Node(3)
    node.left.left.left = Node(4)
    node.left.left.right = Node(4)
    print(get_max_height(node))
    print('Balanced ', balanced(root=node))
