class Solution:
    def addDigits(self, num: int) -> int:
        num = [int(i) for i in str(num)]
        while len(num) > 1:
            n = sum(num)
            num = [int(i) for i in str(n)]

        return num[0]