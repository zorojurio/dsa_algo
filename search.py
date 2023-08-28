from typing import List


def binary_search(array: List, value: int) -> int:
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) //2
        if value > array[mid]:
            left = mid + 1
        elif value < array[mid]:
            right = mid - 1
        else:
            return mid
    return -1


new_list = [i*2 for i in range(1000000)]
# print(new_list)
print(binary_search(new_list, 1000000-2))
