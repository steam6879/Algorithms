# Searching pattern in text using Boyer-Moore algorithm

def bm_match(txt, pat):
    skip = [None] * 256

    for pt in range(256):
        skip[pt] = len(pat)
    
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1

    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0: # 검색 성공
                return pt
            pt -= 1
            pp -= 1
        
        if skip[ord(txt[pt])] > len(pat) - pp:  # 텍스트 문자에 대한 건너뛰기 값이 패턴보다 크면
            pt += skip[ord(txt[pt])]    # 건너뛰기 값만큼 옮김
        
        else:   
            pt += len(pat) - pp     # 패턴의 길이만큼 옮김

    return -1

if __name__ == '__main__':
    s1 = input('Enter the text: ')
    s2 = input('Enter the pattern: ')

    idx = bm_match(s1, s2)

    if idx == -1:
        print('No pattern.')

    else:
        print(f'The pattern is in the text at {idx}th index.')