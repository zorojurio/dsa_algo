

def cal_power_of_number(number, power):
    if power == 0:
        return 1
    elif power < 0:
        return 1 / number * cal_power_of_number(number, power+1)
    return cal_power_of_number(number, power-1) * number


if __name__ == '__main__':
    print(cal_power_of_number(2, -2))
    print(cal_power_of_number(2, 4))
    print(cal_power_of_number(4, 4))
    print(cal_power_of_number(50, 50))
    print(cal_power_of_number(1, 50))
