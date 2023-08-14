

def print_russian_dolls(number):
    if number == 0:
        print(f'All dolls are printed {number}')
    else:
        print(f'Printing doll number {number}')
        return print_russian_dolls(number - 1)


def recursive_number(number):
    if number < 1:
        print('N is less than 1')
    else:
        recursive_number(number-1)
        print(number)


if __name__ == '__main__':
    print_russian_dolls(20)
    recursive_number(20)




