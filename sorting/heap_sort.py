from typing import List


def heapify(custom_list: List, array_size: int, parent_index: int) -> None:
    """
    heapify the heap
    :param custom_list:
    :param array_size:
    :param parent_index:
    :return:
    """
    largest = parent_index
    left_index = parent_index * 2 + 1
    right_index = parent_index * 2 + 2

    if left_index < array_size and custom_list[left_index] > custom_list[largest]:
        largest = left_index

    if right_index < array_size and custom_list[right_index] > custom_list[largest]:
        largest = right_index

    if largest != parent_index:
        custom_list[parent_index], custom_list[largest] = custom_list[largest], custom_list[parent_index]
        heapify(custom_list, array_size, largest)


def heap_sort(custom_list):
    n = len(custom_list)
    cust_range = list(range(int(n / 2) - 1, -1, -1))
    for i in cust_range:
        heapify(custom_list, n, i)

    for i in range(n - 1, 0, -1):
        custom_list[i], custom_list[0] = custom_list[0], custom_list[i]
        heapify(custom_list, i, 0)


if __name__ == '__main__':
    new_list = [10, 20, 60, 40, 80, 5, 15, 20]
    heap_sort(custom_list=new_list)
    print(new_list)