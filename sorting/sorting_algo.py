import math
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


def insertion_sort(my_list: List) -> List:
    for i in range(1, len(my_list)):
        value_to_sort = my_list[i]
        while my_list[i - 1] > value_to_sort and i > 0:
            my_list[i], my_list[i - 1] = my_list[i - 1], my_list[i]
            i -= 1
    return my_list


def bucket_sort(my_list: List) -> List:
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


new_list = [5, 5, 12, 45, 32, 65, 987, 12, 54, 32, 54, 1]
print(bubble_sort(my_list=new_list))
new_list = [5, 5, 12, 45, 32, 65, 987, 12, 54, 32, 54, 1]
print(selection_sort(my_list=new_list))
new_list = [5, 5, 12, 45, 32, 65, 987, 12, 54, 32, 54, 1]
print(insertion_sort(my_list=new_list))
new_list = [5, 5, 12, 45, 32, 65, 987, 12, 54, 32, 54, 1]
print(bucket_sort(my_list=new_list))
