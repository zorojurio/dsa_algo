

def cal_factorial(n):
    if n == 1 or n == 0 or n < 0:
        return 1
    else:
        return cal_factorial(n-1) * n


if __name__ == '__main__':
    print(cal_factorial(4))
    print(cal_factorial(-4))
