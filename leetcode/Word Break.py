from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [True] + [False] * len(s)

        for i in range(1, len(s) + 1):
            for word in wordDict:
                if s[:i].endswith(word):
                    dp[i] = dp[i - len(word)]

                    if dp[i]:
                        break  # Break out as soon as you hit a true value

        return dp[-1]


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Create a set for faster lookup
        word_set = set(wordDict)

        # Initialize a boolean array to track if a substring can be segmented
        dp = [False] * (len(s) + 1)
        dp[0] = True  # An empty string can always be segmented

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[len(s)]

# Test cases
s1 = "leetcode"
wordDict1 = ["leet", "code"]
print(Solution.wordBreak(s1, wordDict1))  # Output: True