def calc_fibonacci(number):
    if number == 0 or number == 1 or number < 0:
        return 1
    else:
        return calc_fibonacci(number - 1) + calc_fibonacci(number - 2)


if __name__ == '__main__':
    print(calc_fibonacci(-5))
    print(calc_fibonacci(5))
# 1 , 2 , 3, 5, 8
