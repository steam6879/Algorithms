def bf_match(txt, pat):
    pt = 0
    pp = 0

    while pt != len(txt) and pp != len(pat):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1

        else:
            pt = pt - pp + 1
            pp = 0
    
    if pp == len(pat):
        return pt - pp
    
    else:
        return -1
    
if __name__ == '__main__':
    s1 = input('text: ')
    s2 = input('pattern: ')

    idx = bf_match(s1, s2)

    if idx == -1:
        print('no pattern')

    else:
        print(f'the first pattern is in {idx + 1}')