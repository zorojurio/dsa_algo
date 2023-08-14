

def print_russian_dolls(number):
    if number == 0:
        print(f'All dolls are printed {number}')
    else:
        print(f'Printing doll number {number}')
        return print_russian_dolls(number - 1)


if __name__ == '__main__':
    print_russian_dolls(20)
