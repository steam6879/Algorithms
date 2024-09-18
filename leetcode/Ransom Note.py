from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = defaultdict(lambda: 0)
        for char in magazine:
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
