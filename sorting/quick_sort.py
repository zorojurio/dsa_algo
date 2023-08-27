from typing import List


def swap(my_list: List, x: int, y: int) -> None:
    my_list[x], my_list[y] = my_list[y], my_list[x]


def pivot_function(my_list: List, pivot_index: int, end_index: int) -> int:
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index):
        if my_list[pivot_index] > my_list[i]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, swap_index, pivot_index)
    return swap_index


def quick_sort(my_list, left, right):
    print(left, right)
    if left < right:
        pivot_index = pivot_function(my_list, left, right)
        quick_sort(my_list, left, pivot_index - 1)
        quick_sort(my_list, pivot_index + 1, right)
    return my_list


new_list = [3, 0, 5, 6, 2, 1, 4]
print(new_list)

quick_sort(new_list, 0, len(new_list))
print(new_list)
