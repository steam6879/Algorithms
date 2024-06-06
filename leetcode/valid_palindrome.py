from collections import deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 자료형 데크로 선언
        strs: deque = deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True


class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = [char.lower() for char in s if char.isalnum()]

        return ans == ans[::-1]
