class Heap:
    def __init__(self, size):
        self.custom_list = [None] * (size + 1)
        self.heap_size = 0
        self.max_size = size + 1  # because we are not using 0th index

    @staticmethod
    def peek_heap(root_node):
        """
        get the value of first index which is root node
        :param root_node:
        :return:
        """
        if not root_node:
            return None
        return root_node.custom_list[1]

    @staticmethod
    def get_heap_size(root_node):
        if not root_node:
            return 0
        return root_node.heap_size

    @staticmethod
    def level_order_traversal(root_node):
        if not root_node:
            return
        for i in range(1, root_node.heap_size + 1):
            print(root_node.custom_list[i], end=", ")

    @classmethod
    def heapify_tree_insert(cls, root_node, index, heap_type):
        parent_index = int(index // 2)
        if index <= 1:
            return
        if heap_type.lower() == 'min':
            if root_node.custom_list[index] < root_node.custom_list[parent_index]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[parent_index]
                root_node.custom_list[parent_index] = temp
            cls.heapify_tree_insert(root_node, parent_index, heap_type)
        elif heap_type.lower() == 'max':
            if root_node.custom_list[index] > root_node.custom_list[parent_index]:
                temp = root_node.custom_list[index]
                root_node.custom_list[index] = root_node.custom_list[parent_index]
                root_node.custom_list[parent_index] = temp
            cls.heapify_tree_insert(root_node, parent_index, heap_type)

    @classmethod
    def insert_node(cls, root_node, node_value, heap_type):
        if root_node.heap_size + 1 == root_node.max_size:
            return "Full"
        root_node.custom_list[root_node.heap_size + 1] = node_value
        root_node.heap_size += 1
        cls.heapify_tree_insert(root_node, root_node.heap_size, heap_type)
        return "Value has been successfully added"

    @classmethod
    def heapify_tree_extract(cls, root_node, index, heap_type):
        left_index = index * 2
        right_index = index * 2 + 1
        swap_child = 0


if __name__ == '__main__':
    heap = Heap(10)
    Heap.insert_node(heap, 10, 'Max')
    Heap.insert_node(heap, 20, 'Max')
    Heap.insert_node(heap, 60, 'Max')
    Heap.insert_node(heap, 40, 'Max')
    Heap.insert_node(heap, 80, 'Max')
    Heap.insert_node(heap, 5, 'Max')
    Heap.insert_node(heap, 50, 'Max')
    Heap.insert_node(heap, 30, 'Max')
    Heap.level_order_traversal(heap)
