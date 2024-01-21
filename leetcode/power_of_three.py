class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        elif n == 1:
            return True
        elif n % 3 == 0:
            return self.isPowerOfThree(n // 3)
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfThree(27))
