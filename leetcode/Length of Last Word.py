class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start, end = 0, 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] != ' ':
                end = i
                break
        
        for i in range(end - 1, -1, -1):
            if s[i] == ' ':
                start = i + 1
                break
        
        return end - start + 1
    
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        wordList = s.split()

        if wordList:
            return len(wordList[-1])
        
        return 0
    
print(Solution.lengthOfLastWord(Solution, s=' a'))