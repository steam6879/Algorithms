class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        resS = []
        resT = []

        for char in list(s):
            if char != '#':
                resS.append(char)
            else:
                if resS:
                    resS.pop()

        for char in list(t):
            if char != '#':
                resT.append(char)
            else:
                if resT:
                    resT.pop()

        return resS == resT
    
class Solution:     #24.5.6. ~ my solution in grind 98
    def backspaceCompare(self, s: str, t: str) -> bool:
        stkS, stkT = [], []
        for char in s:
            if char == '#':
                if not stkS:
                    continue
                stkS.pop()
            else:
                stkS.append(char)

        for char in t:
            if char == '#':
                if not stkT:
                    continue
                stkT.pop()
            else:
                stkT.append(char)

        return stkS == stkT