import math
from typing import List


def bubble_sort(my_list: List) -> List:
    """
    compares adjacent elements, and swaps them if they are in the wrong order,
    :param my_list: list
    :return: my_list: list
    """
    for i in range(len(my_list) - 1):
        for j in range(len(my_list) - 1 - i):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list


def selection_sort(my_list: List) -> List:
    """
    selects the minimum element from an unsorted part of the list and places it at the beginning.
    :param my_list: list
    :return my_list:
    """
    for i in range(len(my_list)):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[min_index] > my_list[j]:
                min_index = j
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]
    return my_list


def insertion_sort(my_list: List) -> List:
    """
     comparing each element with its predecessors and shifting them to the right until the correct position is found.
    :param my_list:
    :return:
    """
    for i in range(1, len(my_list)):
        value_to_sort = my_list[i]
        while my_list[i - 1] > value_to_sort and i > 0:
            my_list[i], my_list[i - 1] = my_list[i - 1], my_list[i]
            i -= 1
    return my_list


def bucket_sort(my_list: List) -> List:
    """
     Elements are distributed into these buckets based on their value ranges, and then each bucket is
     sorted individually, combining the results to produce the sorted output.
    :param my_list:
    :return:
    """
    number_of_buckets = round(math.sqrt(len(my_list)))
    max_value = max(my_list)
    buckets = []
    for i in range(number_of_buckets):
        buckets.append([])

    for j in my_list:
        index_bucket = math.ceil(j * number_of_buckets / max_value)
        buckets[index_bucket - 1].append(j)

    for i in range(number_of_buckets):
        buckets[i] = insertion_sort(buckets[i])

    init_index = 0
    for bucket in buckets:
        for number in bucket:
            my_list[init_index] = number
            init_index += 1
    return my_list


def merge_sort(array: List) -> None:
    length = len(array)
    if len(array) > 1:
        mid_index = len(array) // 2

        left_array = array[:mid_index]
        right_array = array[mid_index:]

        merge_sort(left_array)
        merge_sort(right_array)

        left_index = right_index = sorted_index = 0
        while left_index < len(left_array) and right_index < len(right_array):
            if left_array[left_index] < right_array[right_index]:
                array[sorted_index] = left_array[left_index]
                left_index += 1
            else:
                array[sorted_index] = right_array[right_index]
                right_index += 1
            sorted_index += 1
            
        # Checking if any element was left
        while left_index < len(left_array):
            array[sorted_index] = left_array[left_index]
            left_index += 1
            sorted_index += 1

        while right_index < len(right_array):
            array[sorted_index] = right_array[right_index]
            right_index += 1
            sorted_index += 1


new_list = [5, 5, 12, 45, 32, 65, 987, 12, 54, 32, 54, 1]
print(bubble_sort(my_list=new_list))
new_list = [5, 5, 12, 45, 32, 65, 987, 12, 54, 32, 54, 1]
print(selection_sort(my_list=new_list))
new_list = [5, 5, 12, 45, 32, 65, 987, 12, 54, 32, 54, 1]
print(insertion_sort(my_list=new_list))
new_list = [5, 3, 12, 45, 32, 65, 987, 12, 54, 32, 54, 22]
print(bucket_sort(my_list=new_list))
new_list = [38, 27, 43, 3, 9, 82, 10]
merge_sort(array=new_list)
print(new_list)