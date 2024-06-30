from collections import Counter


class Solution(object):
    def characterReplacement(self, s, k):
        maxLength, maxCount = 0, 0
        counters = Counter()

        for i in range(len(s)):
            counters[s[i]] += 1
            maxCount = max(maxCount, counters[s[i]])

            if maxLength - maxCount >= k:
                counters[s[i - maxLength]] -= 1

            else:
                maxLength += 1

        return maxLength


if __name__ == "__main__":
    print(Solution.characterReplacement(Solution, s="AABABBA", k=1))


# print(characterReplacement("AABABBA", 1))  # Output: 4


class Solution:
    def characterReplacement(s, k):
        # Dictionary to keep track of the count of each letter
        count = {}
        maxLength = 0
        maxCount = 0  # The count of the most frequent character in the current window
        left = 0  # Left pointer for the sliding window

        for right in range(len(s)):
            # Update the count for the current character
            count[s[right]] = count.get(s[right], 0) + 1
            # Update the count of the most frequent character
            maxCount = max(maxCount, count[s[right]])

            # If the current window size minus the count of the most frequent character
            # is greater than k, shrink the window from the left
            if (right - left + 1) - maxCount > k:
                count[s[left]] -= 1
                left += 1

            # Update the maximum length of the window seen so far
            maxLength = max(maxLength, right - left + 1)

        return maxLength

#     # print(characterReplacement("ABAB", 2))  # Output: 4
#     print(characterReplacement("AABABBA", 1))  # Output: 4


# if __name__ == "__main__":
#     print(Solution.characterReplacement(Solution, s='AABABBAA', k=1))