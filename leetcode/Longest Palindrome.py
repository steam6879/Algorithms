class Solution:
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
            if m[i] // 2 == 1:
                oddMap.append(m[i])
            else:
                evenMap.append(m[i])

        ans = max(oddMap) + sum(evenMap)

        return ans
        
if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("abccccdd"))