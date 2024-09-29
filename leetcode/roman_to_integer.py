class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        m = {"I": 1,
             "V": 5,
             "X": 10,
             "L": 50,
             "C": 100,
             "D": 500,
             "M": 1000}

        for i, roman in enumerate(s):
            if i + 1 < len(s) and m[roman] < m[s[i + 1]]:
                ans -= m[roman]

            else:
                ans += m[roman]

        return ans
