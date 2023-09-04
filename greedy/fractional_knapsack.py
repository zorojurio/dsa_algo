from typing import List


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight

    def __str__(self):
        return f'{self.value}: {self.ratio}'


def knapsack_method(item_list: List[Item], desired_value):
    item_list.sort(key=lambda x: x.ratio, reverse=True)
    total = 0
    used_capacity = 0
    for item in item_list:
        print(item)
        if used_capacity + item.weight <= desired_value:
            used_capacity += item.weight
            total += item.value
        else:
            addition = (desired_value - used_capacity) * item.ratio
            used_capacity += (desired_value - used_capacity)
            total += addition
        if used_capacity == desired_value:
            break
    print(total)


item1 = Item(20, 100)
item2 = Item(30, 120)
item3 = Item(10, 60)
c_list = [item1, item2, item3]

knapsack_method(c_list, 50)
