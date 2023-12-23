import copy

def seq_search(seq, key):       #sentinel method(보초법)
    a = copy.deepcopy(seq)
    a.append(key)

    i = 0
    while True:
        if a[i] == key:
            break
        i += 1

    if i == len(seq):
        return -1
    else:
        return i


if __name__ =='__main__':
    num = int(input("Enter a number of element : "))
    x = [None] * num
    for i in range(num):
        x[i] = int(input(f'x[{i}] : '))

    ky = int(input('Enter a key: '))

    idx = seq_search(x, ky)

    if idx == -1:
        print(f'do not exsist {ky}.')

    else:
        print(f'x[{idx}]')