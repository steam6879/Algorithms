class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = {}
        for char in s:
            if char in m:
                m[char] += 1

            else:
                m[char] = 1

        for char in t:
            if char in m:
                m[char] -= 1
                if m[char] < 1:
                    m.pop(char)

            else:
                return False

        return len(m) == 0


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}

        for char in s:
            if char in ds:
                ds[char] += 1

            else:
                ds[char] = 1

        for char in t:
            if char in dt:
                dt[char] += 1

            else:
                dt[char] = 1

        return ds == dt
