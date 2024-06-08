class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        m = set()
        maxLen = 0

        for end in range(len(s)):
            if s[end] in m:
                while s[end] in m:
                    m.remove(s[start])
                    start += 1

                m.add(s[end])

            else:
                m.add(s[end])
                maxLen = max(maxLen, end - start + 1)

        return maxLen
