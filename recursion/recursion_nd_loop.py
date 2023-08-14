

def power_of_two_recursive(number):
    if number == 0:
        return 1
    else:
        power = power_of_two_recursive(number-1)
        return power * 2


def iterate_power_two(number):
    i = 0
    power = 1
    while i < number:
        power = power * 2
        i = i + 1
    return power


if __name__ == '__main__':
    print(power_of_two_recursive(4) == iterate_power_two(4))
