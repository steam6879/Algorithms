def merge_sorted_list(a, b, c):
    pa, pb, pc = 0, 0, 0
    na, nb, nc = len(a), len(b), len(c)

    while pa < na and pb < nb:
        if a[pa] <= b[pb]:
            c[pc] = a[pa]
            pa += 1
        
        else:
            c[pc] = b[pb]
            pb += 1

        pc += 1

    while pa < na:
        c[pc] = a[pa]
        pa += 1
        pc += 1
    
    while pb < nb:
        c[pc] = b[pb]
        pb += 1
        pc += 1


def merge_sort(a):
    def _merge_sort(a, left, right):
        if left < right:
            center = (left + right) // 2

            _merge_sort(a, left, center)
            _merge_sort(a, center + 1, right)

            p = j = 0
            i = k = left

            while i <= center:
                buff[p] = a[i]
                p += 1
                i += 1
            
            while i <= right and j < p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                
                else:
                    a[k] = a[i]
                    i += 1
                k += 1

            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1
    
    n = len(a)
    buff = [None] * n
    _merge_sort(a, 0, n - 1)
    del buff

if __name__ == '__main__': 
    # a = [2, 4, 6, 8, 11, 13]
    # b = [1, 2, 3, 4, 9, 16, 21]
    # c = [None] * (len(a) + len(b))

    # print('merge two sorted list')

    # merge_sorted_list(a, b, c)
    
    # print()
    # print(f'list a: {a}')
    # print(f'list b: {b}')
    # print(f'list c: {c}')

    print('merge sort')
    num = int(input('Enter the number of elements: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: ')) 

    merge_sort(x)

    print('\nascending order')

    for i in range(num):
        print(f'x[{i}] = {x[i]}')