class Solution:
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
    
if __name__ == "__main__":
    s = "a##c"
    t = "#a#c"
    print(Solution.backspaceCompare(Solution, s, t))