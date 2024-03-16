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