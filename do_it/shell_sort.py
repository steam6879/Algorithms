def shell_sort(a):
    n = len(a)
    h = 1   # interval

    while h < n // 9:   # 1, 4, 13, 40, 121, 364, 1093, ...
        h = h * 3 + 1 

    while h > 0:
        for i in range(h, n):
            j = i - h
            tmp = a[i]

            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            
            a[j + h] = tmp
            print(h)
        
        h //= 3

if __name__ == '__main__':
    print('shell sort')
    num = int(input('how many elements do you want to sort?: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    shell_sort(x)

    print('\nascending order')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')