from typing import List


def bubble_sort(my_list: List) -> List:
    for i in range(len(my_list) - 1):
        for j in range(len(my_list) - 1 - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list


def selection_sort(my_list: List) -> List:
    for i in range(len(my_list)):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[min_index] > my_list[j]:
                min_index = j
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return my_list


new_list = [5, 5, 12, 45, 32, 65, 987, 12, 54, 32, 54, 1]
print(bubble_sort(my_list=new_list))
new_list = [5, 5, 12, 45, 32, 65, 987, 12, 54, 32, 54, 1]
print(selection_sort(my_list=new_list))
