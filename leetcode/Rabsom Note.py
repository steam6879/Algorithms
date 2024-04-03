class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = {}
        for char in magazine:
            if char not in m:
                m[char] = 1
            else:
                m[char] += 1

        for char in ransomNote:
            if char in m:
                if m[char] > 0:
                    m[char] -= 1
                else:
                    return False
            
            else:
                return False
            
        else:
            return True