def heap_sort(a):

    def down_heap(a, left, right):
        temp = a[left]  # root

        parent = left
        while parent < (right + 1) // 2:    # while parent is not leaf
            cl = parent * 2 + 1     # left child
            cr = cl + 1        # right child
            
            if cr <= right and a[cr] > a[cl]:
                child = cr
            
            else: child = cl

            if temp >= a[child]:
                break

            a[parent] = a[child]
            parent = child

        a[parent] = temp

    n = len(a)

    for i in range((n - 1) // 2, -1, -1):
        down_heap(a, i, n - 1)

    for i in range(n - 1, 0, -1):
        a[0], a[i] = a[i], a[0]
        down_heap(a, 0, i - 1)

if __name__ == '__main__':
    print('heap sort')
    num = int(input('input number of data: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    heap_sort(x)

    print('\nascending order')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')