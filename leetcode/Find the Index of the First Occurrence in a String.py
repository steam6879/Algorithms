class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
            
        return -1
    
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == '__main__':
    print(Solution.strStr(Solution, 'sadbutsad', 'but'))

        
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ptr = 0
        for char in haystack:
            if char == needle[ptr]:
                ptr += 1
            elif char != needle[ptr]:
                ptr = 0
            elif ptr == len(needle) - 1:
                return needle.index(char) - ptr
            
        return -1