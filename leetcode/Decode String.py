class Solution:
    def decodeString(self, s: str) -> str:
        # 스택을 초기화합니다.
        stack = []
        # 현재 숫자와 현재 문자열을 초기화합니다.
        curNum = 0
        curString = ''

        # 문자열을 하나씩 순회합니다.
        for char in s:
            if char == '[':
                # '['를 만나면 현재 문자열과 숫자를 스택에 추가하고, 현재 문자열과 숫자를 초기화합니다.
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0

            elif char == ']':
                # ']'를 만나면 스택에서 이전 문자열과 숫자를 꺼내어 현재 문자열에 반복해서 추가합니다.
                num = stack.pop()  # 저장해 둔 숫자를 꺼내옵니다.
                prevString = stack.pop()  # 저장해 둔 이전 문자열을 꺼내옵니다.
                curString = prevString + num * curString

            elif char.isdigit():
                # 숫자인 경우 현재 숫자를 업데이트합니다.
                curNum = curNum * 10 + int(char)

            else:
                # 문자인 경우 현재 문자열에 추가합니다.
                curString += char

        # 최종적으로 구한 문자열을 반환합니다.
        return curString


print(Solution.decodeString(Solution, s='3[a2[c]]'))
