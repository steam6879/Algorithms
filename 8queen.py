pos = [0] * 8
flag_a = [False] * 8
flag_b = [False] * 15
flag_c = [False] * 15

def put():
    for i in range(8):
        print(f'{pos[i]:2}', end='')

    print()

def set(i: int) -> None:
    for j in range(8):
        if (not flag_a[j]   # j행에 퀸을 배치하지 않았다면
            and not flag_b[i + j]   # 대각선 방향(↙↗)으로 퀸을 배치하지 않았다면
            and not flag_c[i - j + 7]): # 대각선 방향(↘↖)으로 퀸을 배치하지 않았다면
            
            pos[i] = j
            if i == 7:
                put()
            
            else:
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = True
                set(i + 1)
                flag_a[j] = flag_b[i + j] = flag_c[i - j + 7] = False

set(0)