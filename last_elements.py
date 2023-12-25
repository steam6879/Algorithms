n = int(input('How many elements do you want to store?: '))
a= [None] * n

cnt = 0
while True:
    a[cnt% n] = int(input(f'{cnt + 1} element: '))
    cnt += 1

    retry = input(f'Continue? (Y/N): ')
    if retry in {'N', 'n'}:
        break

i = cnt - n
if i < 0:
    i = 0

while i < cnt:
    print(f'{i + 1} element = {a[i % n]}')
    i += 1
    