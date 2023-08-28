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
        if not root_node.custom_list:
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
    def heapify_tree_extract(cls, root_node, parent_index, heap_type):
        left_index = parent_index * 2
        right_index = parent_index * 2 + 1

        if root_node.heap_size < left_index:  # check if the tree has children
            return
        elif root_node.heap_size == left_index:   # only one child that is left child
            if heap_type == "Min":
                if root_node.custom_list[parent_index] > root_node.custom_list[left_index]:
                    # MIN HEAP, parents value is higher than left children value, hence swapping values
                    temp = root_node.custom_list[parent_index]
                    root_node.custom_list[parent_index] = root_node.custom_list[left_index]
                    root_node.custom_list[left_index] = temp
                return
            else:
                if root_node.custom_list[parent_index] < root_node.custom_list[left_index]:
                    # MAX HEAP, parents value is less than left children value, hence swapping values
                    temp = root_node.custom_list[parent_index]
                    root_node.custom_list[parent_index] = root_node.custom_list[left_index]
                    root_node.custom_list[left_index] = temp
                return

        else:
            # Case where root node has two children
            if heap_type == "Min":
                # MIN HEAP, find the minimum and replace with the root node
                if root_node.custom_list[left_index] < root_node.custom_list[right_index]:
                    # if the left value is less, swap child will be left child
                    swap_index = left_index
                else:
                    # if the right value is less, swap child will be left child
                    swap_index = right_index

                if root_node.custom_list[parent_index] > root_node.custom_list[swap_index]:
                    # replace the smallest with parent
                    # MIN HEAP, if parent value > min(left_child, right_child), Hence Swapping
                    temp = root_node.custom_list[parent_index]
                    root_node.custom_list[parent_index] = root_node.custom_list[swap_index]
                    root_node.custom_list[swap_index] = temp
            else:
                # MAX HEAP, find the maximum nad replace with the root node
                # swap_index = max(left_child, right_child)
                if root_node.custom_list[left_index] > root_node.custom_list[right_index]:
                    # if the left value is Greater, swap child will be left child
                    swap_index = left_index
                else:
                    # if the right value is greater, swap child will be left child
                    swap_index = right_index
                if root_node.custom_list[parent_index] < root_node.custom_list[swap_index]:
                    # replace the largest with parent
                    # MIN HEAP, if parent value < max(left_child, right_child), Hence Swapping
                    temp = root_node.custom_list[parent_index]
                    root_node.custom_list[parent_index] = root_node.custom_list[swap_index]
                    root_node.custom_list[swap_index] = temp
        cls.heapify_tree_extract(root_node, swap_index, heap_type)

    @classmethod
    def extract_node(cls, root_node, heap_type):
        if root_node.heap_size == 0:
            return
        else:
            extracted_node = root_node.custom_list[1]
            root_node.custom_list[1] = root_node.custom_list[root_node.heap_size]
            root_node.custom_list[root_node.heap_size] = None
            root_node.heap_size -= 1
            cls.heapify_tree_extract(root_node, 1, heap_type)
            return extracted_node

    @classmethod
    def delete_entire_binary_heap(cls, root_node):
        root_node.custom_list = None


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
    Heap.extract_node(heap, "Max")
    Heap.level_order_traversal(heap)
    Heap.delete_entire_binary_heap(heap)
    Heap.level_order_traversal(heap)
