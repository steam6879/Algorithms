class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        elif len(s) == 2:
            if s[0] == s[1]:
                return s
            else:
                return s[0]
        ans = ''
        left, mid, right = 0, 1, 2

        while right < len(s):
            if s[left] == s[right]:
                while s[left] == s[right]:
                    if left < 1:
                        break
                    left -= 1

                    if right > len(s) - 2:
                        break
                    right += 1

                if (right - left - 1) > len(ans):
                    ans = s[left + 1 : right]

            mid += 1
            left, right = mid - 1, mid + 1

        return ans


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        maxStr = s[0]

        for i in range(len(s) - 1):
            odd = expand(i, i)
            even = expand(i, i + 1)

            if len(odd) > len(maxStr):
                maxStr = odd
            if len(even) > len(maxStr):
                maxStr = even

        return maxStr


if __name__ == "__main__":
    print(Solution.longestPalindrome(Solution, s='abcdanananananbcac'))