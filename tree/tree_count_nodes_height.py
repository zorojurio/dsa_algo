
class Node:

    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.item}'

    def __repr__(self):
        return f'{self.item}'


def count_nodes(root_node: Node):
    if root_node is None:
        return 0
    else:
        left_nodes = count_nodes(root_node.left)
        right_nodes = count_nodes(root_node.right)
        all_nodes = 1 + left_nodes + right_nodes
        return all_nodes


def get_max_height(root_node: Node):
    if root_node is None:
        return 0
    left_height = get_max_height(root_node.left)
    right_height = get_max_height(root_node.right)
    max_height = 1 + max(left_height, right_height)
    return max_height


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(f'Total Count Of Nodes {count_nodes(root_node=root)}')
print(f'Height of Root Node {get_max_height(root_node=root)}')
