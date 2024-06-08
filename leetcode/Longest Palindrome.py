from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counters = Counter(s)

        evens = [value for value in counters.value() if value % 2 == 0]
        odds = [value for value in counters.value() if value % 2 != 0]

        if odds:
            useOdds = sum(odds) - (len(odds) - 1)
            return sum(evens) + useOdds
        else:
            return sum(evens)


class Solution:     #uncorrect code
    def longestPalindrome(self, s: str) -> int:
        if len(s) < 2:
            return 1
        
        m = {}
        for char in s:
            if char in m:
                m[char] += 1
            else:
                m[char] = 1

        evenMap = []
        oddMap = []
        for i in m:
            if m[i] % 2 == 1:
                oddMap.append(m[i])
            else:
                evenMap.append(m[i])
        if len(oddMap) < 1:
            ans = sum(evenMap)
        else:
            ans = max(oddMap) + sum(evenMap)

        return ans


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
    s = Solution()
    print(s.longestPalindrome("abccccdd"))