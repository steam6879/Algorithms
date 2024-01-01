# from stack import Stack
# from insertion_sort import insertion_sort
from typing import MutableSequence, Any

def partition(a):
    n = len(a)
    pl = 0
    pr = n - 1
    x = a[n // 2]

    while pl <= pr:
        while a[pl] < x:
            pl += 1
        
        while a[pr] > x:
            pr -= 1

        if pl <= pr:
            a[pl], a[pr] = a[pr], a[pl]
            pl += 1
            pr -= 1

    print(f'pivot: {x}')

    print('Group less than or equal to pivot')
    print(*a[0 : pl])   # * is used to print the list without brackets

    if pl > pr + 1:
        print('Group equal to pivot')
        print(*a[pr + 1 : pl]) 

    print('Group greater than pivot')
    print(*a[pr + 1 : n])

def sort3(a, idx1, idx2, idx3):
    if a[idx2] < a[idx1]:
        a[idx2], a[idx1] = a[idx1], a[idx2]
    
    if a[idx3] < a[idx2]:
        a[idx3], a[idx2] = a[idx2], a[idx3]

    if a[idx2] < a[idx1]:
        a[idx2], a[idx1] = a[idx1], a[idx2]

    return idx2

def insertion_sort(a: MutableSequence, left, right) -> None:
    for i in range(1, left + 1, right + 1):
        j = i
        tmp = a[i]

        while j > 0 and a[j - 1] > tmp:
            a[j] = a[j - 1]
            j -= 1

        a[j] = tmp


def qsort(a, left, right):
    if right - left < 9:
        insertion_sort(a, left, right)

    else:
        pl = left
        pr = right
        m = sort3(a, pl, (pl + pr) // 2, pr)
        x = a[m]

        a[m], a[pr - 1] = a[pr - 1], a[m]
        pl += 1
        pr -= 2

        while pl <= pr:
            while a[pl] < x:
                pl += 1
            
            while a[pr] > x:
                pr -= 1

            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        if left < pr:
            qsort(a, left, pr)

        if pl < right:
            qsort(a, pl, right)

def quick_sort(a):
    qsort(a, 0, len(a) - 1)


# def non_recursive_qsort(a, left, right):
#     range = Stack(right - left + 1)

#     range.push((left, right))

#     while not range.is_empty():
#         pl, pr = left, right = range.pop()
#         x = a[(left + right) // 2]

#         while pl <= pr:
#             while a[pl] < x:
#                 pl += 1
            
#             while a[pr] > x:
#                 pr -= 1

#             if pl <= pr:
#                 a[pl], a[pr] = a[pr], a[pl]
#                 pl += 1
#                 pr -= 1

#         if left < pr:
#             range.push((left, pr))
#         if pl < right:
#             range.push((pl, right))

# def non_recursive_quick_sort(a):
#     non_recursive_qsort(a, 0, len(a) - 1)



if __name__ == '__main__':
    print('quick sort')
    num = int(input('how many elements do you want to sort?: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    quick_sort(x)

    print('\nascending order')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
