class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1, num2 = num1[::-1], num2[::-1]

        if len(num1) < len(num2):
            num1 += '0' * (len(num2) - len(num1))
        else:
            num2 += '0' * (len(num1) - len(num2))

        result = ''
        carry = 0

        for i in range(len(num1)):
            digitSum = int(num1[i]) + int(num2[i]) + carry
            carry = digitSum // 10
            result += str(digitSum % 10)

        if carry > 0:
            result += str(carry)

        return result[::-1]