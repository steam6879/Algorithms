class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hayPtr, needlePtr = 0, 0
        for char in haystack:
            if char == needle[needlePtr]:
                needlePtr += 1
            elif char != needle[needlePtr]:
                ptr = 0
            elif needlePtr == len(needle) - 1:
                return 

        
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