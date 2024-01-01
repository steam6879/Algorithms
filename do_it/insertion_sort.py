from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    n = len(a)

    for i in range(1, n):
        j = i
        tmp = a[i]

        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1
            print(a)

        a[j] = tmp

if __name__ == '__main__':
    print('insertion sort')
    num = int(input('how many elements do you want to sort?: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    insertion_sort(x)

    print('\nascending order')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
