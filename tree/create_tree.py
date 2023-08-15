class TreeNode:
    def __init__(self, data, children=None):
        if children is None:
            children = []
        self.data = data
        self.children = children

    def __str__(self, level=0):
        value = f"{' '* level} {self.data} \n"
        for child in self.children:
            value += child.__str__(level + 1)
        return value

    def add_child(self, child_node):
        self.children.append(child_node)


if __name__ == '__main__':
    tree = TreeNode('Drinks')
    cold = TreeNode('Cold')
    hot = TreeNode('Hot')
    tree.add_child(cold)
    tree.add_child(hot)
    tea = TreeNode('tea')
    coffee = TreeNode('coffee')
    cola = TreeNode('cola')
    fanta = TreeNode('fanta')
    soda = TreeNode('soda')
    hot.add_child(tea)
    hot.add_child(coffee)
    cold.add_child(fanta)
    cold.add_child(soda)
    cold.add_child(cola)
    print(tree)
