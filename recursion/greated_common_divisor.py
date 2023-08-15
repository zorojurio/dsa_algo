

def cal_common_factor(a, b):
    if a < 0:
        a = a * -1
    if b < 0:
        b = b * -1
    if b == 0:
        return a
    else:
        return cal_common_factor(b, a%b)


if __name__ == '__main__':
    print(cal_common_factor(48, 18))
    print(cal_common_factor(8, -12))
