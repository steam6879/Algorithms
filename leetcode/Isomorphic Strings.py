class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}

        for char in s:
            if char in hashS:
                hashS[char] += 1
            else:
                hashS[char] = 1
        listS = [value for value in hashS.values()]
            
        for char in t:
            if char in hashT:
                hashT[char] += 1
            else:
                hashT[char] = 1
        listT = [value for value in hashT.values()]

        return sorted(listS)[:] == sorted(listT)[:]
    

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCheck = []
        tCheck = []

        for char in s:
            sCheck.append(s.index(char))

        for char in t:
            tCheck.append(t.index(char))

        if sCheck == tCheck:
            return True
        else:
            return False