from functools import lru_cache


@lru_cache(251)
def calc_fibonacci(number):
    if number == 0 or number == 1 or number < 0:
        return number
    else:
        return calc_fibonacci(number - 1) + calc_fibonacci(number - 2)


if __name__ == '__main__':
    print(calc_fibonacci(-5))
    fib_series = [calc_fibonacci(i) for i in range(250)]
    print(fib_series)
    print(len(fib_series))
# 1 , 2 , 3, 5, 8
