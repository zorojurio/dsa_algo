

def cal_sum_of_digits(number):
    if number < 10:
        return number
    return number % 10 + cal_sum_of_digits(number//10)


if __name__ == '__main__':
    print(cal_sum_of_digits(99999))
