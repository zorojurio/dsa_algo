
class Node:

    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


def count_nodes(root_node: Node):
    if root_node is None:
        return 0
    else:
        return 1 + count_nodes(root_node.left) + count_nodes(root_node.right)


def get_max_height(root_node: Node):
    if root_node is None:
        return 0
    return 1 + max(get_max_height(root_node.left), get_max_height(root_node.right))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print(f'Total Count Of Nodes {count_nodes(root_node=root)}')
print(f'Height of Root Node {get_max_height(root_node=root)}')
