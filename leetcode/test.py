from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        m = Counter(s)
        odd, even = [], []
        count = 0

        for key in m:
            if m[key] % 2 == 0:
                even.append(m[key])
            else:
                odd.append(m[key])

        count += sum(even)

        if odd:
            count += max(odd)
            odd.remove(max(odd))

            for num in odd:
                count += num - 1

        return count

if __name__ == "__main__":
    print(Solution.longestPalindrome(Solution, s="adam"))