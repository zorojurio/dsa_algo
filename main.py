from typing import List


def bubble_sort(my_list: List[int]) -> List[int]:
    for i in range(len(my_list)):
        for j in range(len(my_list)-1):
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
    return my_list


def selection_sort(my_list: List[int]) -> List[int]:
    for i in range(len(my_list)):
        for j in range(i, len(my_list)):
            if my_list[i] > my_list[j]:
                my_list[i], my_list[j] = my_list[j],  my_list[i]
    return my_list


new_list = [3, 8, 8, 5, 6, 1, 2, 3, 5, 74, 55]

print(selection_sort(my_list=new_list))
