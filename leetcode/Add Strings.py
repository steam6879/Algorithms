class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]

        if len(num1) < len(num2):
            num1 += '0' * (len(num2) - len(num1))
            