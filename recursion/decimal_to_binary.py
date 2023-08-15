

def decimal_to_bin(number):
    if number < 0:
        return 0
    if number == 1:
        return 1
    else:
        return number % 2 + decimal_to_bin(int(number/2)) * 10


if __name__ == '__main__':
    print(decimal_to_bin(13))
    print(decimal_to_bin(10))
    print(decimal_to_bin(3))
